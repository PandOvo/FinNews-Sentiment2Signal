from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[0]  # 使用父级目录作为项目根目录
DATA_RAW = BASE_DIR / "data" / "raw"  # 正确指向 FinNews-Sentiment2Signal/data/raw 文件夹
DATA_INTERIM = BASE_DIR / "data" / "interim"
DATA_PROCESSED = BASE_DIR / "data" / "processed"
OUTPUT_DIR = BASE_DIR / "output"
FIG_DIR = OUTPUT_DIR / "figures"
TAB_DIR = OUTPUT_DIR / "tables"

# Files
NEWS_FILE = DATA_RAW / "news_sample.csv"
MARKET_FILE = DATA_RAW / "market_sample.csv"


# Modeling params
SENTIMENT_METHOD = "lexicon"  # 'lexicon' | 'transformer' (optional)
LAG_DAYS = 1  # assume sentiment at t impacts return at t+1
STRAT_UPPER_Q = 0.7
STRAT_LOWER_Q = 0.3
TRADING_COST_BPS = 5  # per trade, single side

