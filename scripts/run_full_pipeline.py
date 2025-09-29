import pandas as pd
from pathlib import Path
from src.config import FIG_DIR, TAB_DIR, SENTIMENT_METHOD, STRAT_UPPER_Q, STRAT_LOWER_Q, TRADING_COST_BPS
from src.data_loader import load_news, load_market
from src.sentiment_lexicon import score_text as score_lex
from src.sentiment_transformer import score_text_transformer as score_trf
from src.feature_engineering import aggregate_daily_sentiment, make_market_features
from src.evaluation import corr_and_ic
from src.backtest import threshold_timing
from src.plotting import plot_sentiment_vs_market, plot_equity_curves

FIG_DIR.mkdir(parents=True, exist_ok=True)
TAB_DIR.mkdir(parents=True, exist_ok=True)

print("1) Load data ...")
df_news = load_news()
df_mkt = load_market()

print("2) Score sentiments ...")
if SENTIMENT_METHOD == "lexicon":
    df_news['score'] = df_news['text'].apply(score_lex)
else:
    df_news['score'] = df_news['text'].apply(score_trf)

print("3) Aggregate daily sentiment ...")
df_sent = aggregate_daily_sentiment(df_news[['date','score']])

print("4) Market features & merge ...")
df_mkt_f = make_market_features(df_mkt)
df = pd.merge(df_mkt_f, df_sent, on='date', how='left').sort_values('date')
df[['sent_score_mean','sent_pos_ratio','sent_net']] = df[['sent_score_mean','sent_pos_ratio','sent_net']].fillna(0.0)

print("5) Evaluation (corr/IC) ...")
metrics = corr_and_ic(df)
pd.DataFrame([metrics]).to_csv(TAB_DIR / "metrics.csv", index=False)
print(metrics)

print("6) Backtest simple timing ...")
strat_df, perf = threshold_timing(df, signal_col='sent_net', upper_q=STRAT_UPPER_Q, lower_q=STRAT_LOWER_Q, cost_bps=TRADING_COST_BPS)
pd.DataFrame([perf]).to_csv(TAB_DIR / "backtest_perf.csv", index=False)
strat_df.to_csv(TAB_DIR / "backtest_timeseries.csv", index=False)
print(perf)

print("7) Plots ...")
plot_sentiment_vs_market(df, FIG_DIR / "sentiment_vs_market.png")
plot_equity_curves(strat_df, FIG_DIR / "equity_curves.png")

print("Done. Check output/figures and output/tables.")
