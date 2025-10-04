import pandas as pd
import numpy as np

def threshold_timing(df: pd.DataFrame, signal_col: str, upper_q=0.7, lower_q=0.3, cost_bps=5):
    df = df.dropna(subset=[signal_col, 'ret_1d']).copy()
    up = df[signal_col].quantile(upper_q)
    low = df[signal_col].quantile(lower_q)

    pos = []
    last = 0
    for v in df[signal_col].values:
        if v > up:
            last = 1
        elif v < low:
            last = 0
        pos.append(last)
    df['pos'] = pos
    df['trade'] = df['pos'].diff().fillna(0).abs()
    df['strat_ret_gross'] = df['pos'] * df['ret_1d']
    cost = cost_bps / 10000.0
    df['strat_ret_net'] = df['strat_ret_gross'] - df['trade'] * cost
    perf = {
        'gross_cumret': (1 + df['strat_ret_gross']).prod() - 1,
        'net_cumret': (1 + df['strat_ret_net']).prod() - 1,
        'buyhold_cumret': (1 + df['ret_1d']).prod() - 1,
        'turnover': df['trade'].sum() / len(df)  # trades per day
    }
    return df, perf
