# Optional: placeholder for transformer-based inference.
# To keep this template lightweight, we implement a safe stub that returns 0.0.
# You can replace with a real HF pipeline, e.g.:
# from transformers import pipeline
# clf = pipeline('text-classification', model='ProsusAI/finbert')

def score_text_transformer(text: str) -> float:
    # Return neutral by default to avoid dependency issues in demo
    return 0.0
