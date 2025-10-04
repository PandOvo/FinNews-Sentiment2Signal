import pandas as pd
import numpy as np
from config import LAG_DAYS

def aggregate_daily_sentiment(df_news_scored: pd.DataFrame) -> pd.DataFrame:
    # df_news_scored: date, score
    grp = df_news_scored.groupby('date').agg(
        sent_score_mean=('score', 'mean'),
        sent_pos_ratio=('score', lambda s: (s > 0).mean() if len(s)>0 else 0.0),
        sent_net=('score', lambda s: np.sign(s).mean() if len(s)>0 else 0.0),
        n_items=('score', 'count')
    ).reset_index()
    return grp

def make_market_features(df_mkt: pd.DataFrame) -> pd.DataFrame:
    df = df_mkt.copy()
    df['ret_1d'] = df['close'].pct_change()
    df['vol_chg'] = df['volume'].pct_change()
    df['volatility_5d'] = df['close'].pct_change().rolling(5).std()
    # forward returns for labels
    df['fwd_ret_1d'] = df['close'].pct_change().shift(-LAG_DAYS)
    return df
