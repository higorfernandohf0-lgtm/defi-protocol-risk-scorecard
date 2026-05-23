from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

INPUT_PATH = ROOT / "data" / "protocol_scores.csv"
OUTPUT_PATH = ROOT / "reports" / "risk_scorecard.md"


def format_usd(value):
    return f"${value:,.0f}"


def main():

    df = pd.read_csv(INPUT_PATH)

    df = df.sort_values(by="total_score", ascending=False)

    lines = []

    lines.append("# DeFi Protocol Risk Scorecard\n")

    lines.append(
        "This report compares DeFi protocols using public risk indicators.\n"
    )

    lines.append("## Methodology\n")

    lines.append(
        "Each protocol receives a score from 0 to 100 based on:\n"
    )

    lines.append("- TVL Score: 25 points")
    lines.append("- TVL Stability: 20 points")
    lines.append("- Protocol Age: 20 points")
    lines.append("- Holder Concentration: 20 points")
    lines.append("- Audit / Exploit History: 15 points\n")

    lines.append("## Risk Levels\n")

    lines.append("- 80–100: Low Risk")
    lines.append("- 60–79: Medium Risk")
    lines.append("- 0–59: High Risk\n")

    lines.append("## Results\n")

    lines.append("| Protocol | Category | TVL | Score | Risk |")
    lines.append("|---|---|---:|---:|---|")

    for _, row in df.iterrows():

        tvl = format_usd(row["tvl"])

        lines.append(
            f"| {row['name']} | "
            f"{row['category']} | "
            f"{tvl} | "
            f"{row['total_score']} | "
            f"{row['risk_level']} |"
        )

    lines.append("\n## Key Insights\n")

    lines.append(
        "- All selected protocols scored as Low Risk because they are large, mature DeFi protocols."
    )

    lines.append(
        "- Aave achieved the highest score due to strong TVL, stability, and maturity."
    )

    lines.append(
        "- Curve had the lowest score among the group, mainly due to lower TVL compared with the others."
    )

    lines.append(
        "- This MVP uses public indicators and manual inputs for holder concentration and audit/exploit history.\n"
    )

    lines.append("## Disclaimer\n")

    lines.append(
        "This project is for educational and research purposes only. It is not financial advice.\n"
    )

    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")

    print(f"Report generated at {OUTPUT_PATH}")


if __name__ == "__main__":
    main()