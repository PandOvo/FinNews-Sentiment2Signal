import re
from text_clean import basic_clean

POS_WORDS = {
    "beat", "improves", "support", "boosts", "confidence", "accelerate",
    "raise", "optimism", "growth", "profit", "strong", "稳", "利好", "上涨", "提振"
}
NEG_WORDS = {
    "tensions", "risk-off", "miss", "downgrades", "concerns", "volatility",
    "slowdown", "loss", "weak", "下跌", "利空", "紧张", "下行", "抛售"
}

def score_text(text: str) -> float:
    t = basic_clean(text).lower()
    if not t:
        return 0.0
    tokens = set(re.findall(r"[a-zA-Z]+|[\u4e00-\u9fa5]+", t))
    pos = len(tokens & POS_WORDS)
    neg = len(tokens & NEG_WORDS)
    if pos == 0 and neg == 0:
        return 0.0
    return (pos - neg) / max(1, (pos + neg))
