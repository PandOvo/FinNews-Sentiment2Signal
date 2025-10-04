import matplotlib.pyplot as plt
import numpy as np


def calculate_performance(df):
    # 计算年化收益率
    annualized_return = (1 + df['strat_ret_net']).prod() ** (252 / len(df)) - 1  # 252交易日
    # 最大回撤
    max_drawdown = (df['strat_ret_net'].cumprod() - df['strat_ret_net'].cumprod().cummax()).min()
    # 夏普比率
    sharpe_ratio = df['strat_ret_net'].mean() / df['strat_ret_net'].std() * np.sqrt(252)

    return annualized_return, max_drawdown, sharpe_ratio


def plot_sentiment_vs_market(df, fig_path):
    """
    This function plots the sentiment score vs market close price.
    """
    plt.figure(figsize=(10, 6))
    ax1 = plt.gca()

    # Plot Market Close Price
    ax1.plot(df['date'], df['close'], label='Market Close', color='blue')
    ax1.set_ylabel('Market Close')
    ax1.set_xlabel('Date')

    # Create a second y-axis for Sentiment Net
    ax2 = ax1.twinx()
    ax2.plot(df['date'], df['sent_net'], label='Sentiment Net', color='orange')
    ax2.set_ylabel('Sentiment Net')

    ax1.set_title('Sentiment vs Market')

    # Calculate Pearson correlation between sentiment and market
    sentiment_vs_market_corr = df['sent_net'].corr(df['close'])
    plt.text(0.05, 0.95, f"Sentiment-Market Correlation: {sentiment_vs_market_corr:.2f}", transform=plt.gca().transAxes)

    plt.tight_layout()
    plt.savefig(fig_path, dpi=150)
    plt.close()


def plot_equity_curves(df, fig_path):
    """
    This function plots the equity curves for both strategy and buy&hold.
    """
    plt.figure(figsize=(10, 6))

    # Plot Cumulative Returns for Buy & Hold
    (1 + df['ret_1d']).cumprod().plot(label='Buy & Hold', color='blue')
    # Plot Cumulative Returns for Strategy
    (1 + df['strat_ret_net']).cumprod().plot(label='Strategy (Net)', color='orange')

    # Calculate key performance metrics
    annualized_return, max_drawdown, sharpe_ratio = calculate_performance(df)

    # Add key performance metrics to the plot
    plt.text(0.05, 0.95, f"Annualized Return: {annualized_return:.2%}", transform=plt.gca().transAxes)
    plt.text(0.05, 0.90, f"Max Drawdown: {max_drawdown:.2%}", transform=plt.gca().transAxes)
    plt.text(0.05, 0.85, f"Sharpe Ratio: {sharpe_ratio:.2f}", transform=plt.gca().transAxes)

    plt.legend()
    plt.title('Equity Curves')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Returns')
    plt.tight_layout()
    plt.savefig(fig_path, dpi=150)
    plt.close()

