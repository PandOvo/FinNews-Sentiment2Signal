import pandas as pd
import numpy as np

def corr_and_ic(df_merged: pd.DataFrame):
    out = {}
    for col in ['sent_score_mean', 'sent_pos_ratio', 'sent_net']:
        if col in df_merged and 'ret_1d' in df_merged:
            out[f'corr_{col}_ret_1d'] = df_merged[col].corr(df_merged['ret_1d'])
        if col in df_merged and 'fwd_ret_1d' in df_merged:
            out[f'ic_{col}_fwd_ret_1d'] = df_merged[col].corr(df_merged['fwd_ret_1d'])
    return out

def corr_and_ic(df):
    # 计算情感分数与市场的皮尔逊相关系数
    sentiment_vs_market_corr = df['sent_net'].corr(df['close'])
    print(f"Correlation between Sentiment and Market: {sentiment_vs_market_corr:.2f}")

    return {'sentiment_vs_market_corr': sentiment_vs_market_corr}
