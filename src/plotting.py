import matplotlib.pyplot as plt

def plot_sentiment_vs_market(df, fig_path):
    plt.figure()
    ax1 = plt.gca()
    ax1.plot(df['date'], df['close'], label='Close')
    ax1.set_ylabel('Index Close')
    ax1.set_xlabel('Date')
    ax2 = ax1.twinx()
    ax2.plot(df['date'], df['sent_net'], label='Sentiment Net')
    ax2.set_ylabel('Sentiment Net')
    ax1.set_title('Sentiment vs Market')
    plt.tight_layout()
    plt.savefig(fig_path, dpi=150)
    plt.close()

def plot_equity_curves(df, fig_path):
    plt.figure()
    (1+df['ret_1d']).cumprod().plot()
    (1+df['strat_ret_net']).cumprod().plot()
    plt.legend(['Buy&Hold', 'Strategy(Net)'])
    plt.title('Equity Curves')
    plt.xlabel('Date')
    plt.tight_layout()
    plt.savefig(fig_path, dpi=150)
    plt.close()
