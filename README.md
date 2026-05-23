# DeFi Protocol Risk Scorecard

This project analyzes DeFi protocols using public risk indicators and creates a simple risk scoring framework.

## Objective

Build a lightweight DeFi risk assessment model using public on-chain and protocol data.

The project compares protocols based on:

- TVL (Total Value Locked)
- TVL stability over 30 days
- Protocol age
- Holder concentration
- Audit / exploit history

## Risk Methodology

Each protocol receives a score from 0 to 100.

| Metric | Max Points |
|---|---:|
| TVL Score | 25 |
| TVL Stability | 20 |
| Protocol Age | 20 |
| Holder Concentration | 20 |
| Audit / Exploit History | 15 |

## Risk Levels

- 80–100 → Low Risk
- 60–79 → Medium Risk
- 0–59 → High Risk

## Project Structure

```text
defi-protocol-risk-scorecard/
│
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
│
├── config/
│   └── protocols.csv
│
├── scripts/
│   ├── fetch_defillama.py
│   ├── calculate_score.py
│   └── generate_report.py
│
├── data/
│   └── protocol_scores.csv
│
└── reports/
    └── risk_scorecard.md
```

## Stack

- Python
- Pandas
- DeFiLlama API
- Public DeFi Data

## Features

- Fetches DeFi protocol TVL data
- Calculates risk scores automatically
- Generates CSV outputs
- Creates automated Markdown reports
- Compares DeFi protocol risk levels

## Example Output

| Protocol | Score | Risk |
|---|---:|---|
| Aave | 94 | Low |
| Maker | 91 | Low |
| Uniswap | 86 | Low |
| Lido | 85 | Low |
| Curve | 81 | Low |

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Fetch DeFiLlama data:

```bash
python scripts/fetch_defillama.py
```

Calculate scores:

```bash
python scripts/calculate_score.py
```

Generate report:

```bash
python scripts/generate_report.py
```

## Disclaimer

This project is for educational and research purposes only.

It does not constitute financial advice.
