# FinNews-Sentiment2Signal

*From headlines to signals: a reproducible pipeline that transforms financial news sentiment into market insights and simple timing strategies (NLP + Market Data, Python).*

## 项目简介
这是一个“AI+金融”的端到端探索项目：基于金融新闻/公告的情感分析（词典/Transformers/LLM 可拓展），构建日度情绪指数，并与指数价格/成交量进行相关（corr）、信息含量（IC）与简易择时回测。项目强调严谨的时间对齐与可复现性。

**一句话业务价值**：通过金融新闻情感指数，捕捉市场波动前的情绪信号。

## 目录结构
```
ai-fin-nlp-sentiment-predict/
├─ env/
│  └─ environment.yml
├─ data/
│  ├─ raw/ (示例数据：news_sample.csv, market_sample.csv)
│  ├─ interim/
│  └─ processed/
├─ output/
│  ├─ figures/ (示例图自动生成)
│  └─ tables/  (评估表自动生成)
├─ run_full_pipeline.py
├─ *.py (模块化源码)
└─ README.md


## 快速开始
1. **创建环境**（任选其一）：
   ```bash
   # Conda
   conda env create -f env/environment.yml
   conda activate finnews-sentiment2signal
   # 或者 pip
   python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. **运行一键脚本**
   ```bash
   python run_full_pipeline.py
   ```
   输出图表与表格见 `output/figures/` 与 `output/tables/`。

## 数据来源
- 演示使用**合成新闻数据**与**合成市场数据**（`data/raw/*_sample.csv`）。
- 可替换为：公开新闻摘要/公告 + yfinance 等市场数据。

## 方法与评估
- **情感打分**：默认词典法（可拓展 Transformers/LLM）。
- **指标**：相关（corr）、信息含量（IC=与未来收益的相关）、滚动可视化。
- **策略**：基于 `sent_net` 的分位数阈值择时，含交易成本（bps）。

## 主要结果（示例）
运行后将生成：
- `output/figures/sentiment_vs_market.png`：情感指数与价格对比图<img width="1500" height="900" alt="sentiment_vs_market" src="https://github.com/user-attachments/assets/09d7ca19-ae73-4f4a-98b8-8ce81688e3bc" />


- `output/figures/equity_curves.png`：择时策略 vs Buy&Hold 的资金曲线<img width="1500" height="900" alt="equity_curves" src="https://github.com/user-attachments/assets/22b4e88b-22a6-482f-9d8a-09144269f594" />


- `output/tables/metrics.csv`：相关/IC 指标
- `output/tables/backtest_perf.csv`：回测绩效摘要

## 局限性
- 新闻覆盖与发布时间戳可能与交易时段错配；
- 中文金融语义复杂，词典法偏弱；
- 小样本/短样本导致稳定性有限；

## 未来改进
- 使用开源金融情感模型（如 FinBERT/中文 RoBERTa）或指令微调 LLM；
- 引入新闻重要度/权重（来源、热度、公司级别实体识别）；
- 更细的事件研究（Earnings/政策/并购）；
- 多因子融合与更严谨的时序交叉验证；
- 更完善的交易成本建模与滑点模拟。
