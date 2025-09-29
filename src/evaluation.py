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
