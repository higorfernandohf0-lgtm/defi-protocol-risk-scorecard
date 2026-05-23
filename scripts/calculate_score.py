import pandas as pd
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = ROOT / "data" / "defillama_raw.csv"
OUTPUT_PATH = ROOT / "data" / "protocol_scores.csv"


def tvl_score(tvl):
    if tvl >= 10_000_000_000:
        return 25
    elif tvl >= 5_000_000_000:
        return 22
    elif tvl >= 1_000_000_000:
        return 18
    elif tvl >= 500_000_000:
        return 14
    elif tvl >= 100_000_000:
        return 10
    else:
        return 5


def stability_score(change):
    if pd.isna(change):
        return 8
    if change >= 0:
        return 20
    elif change >= -5:
        return 17
    elif change >= -15:
        return 13
    elif change >= -30:
        return 8
    else:
        return 4


def age_score(launch_year):
    current_year = datetime.now().year
    age = current_year - int(launch_year)

    if age >= 6:
        return 20
    elif age >= 4:
        return 17
    elif age >= 2:
        return 13
    elif age >= 1:
        return 8
    else:
        return 4


def risk_level(total_score):
    if total_score >= 80:
        return "Low"
    elif total_score >= 60:
        return "Medium"
    else:
        return "High"


def main():
    df = pd.read_csv(INPUT_PATH)

    df["tvl_score"] = df["tvl"].apply(tvl_score)
    df["stability_score"] = df["tvl_30d_change"].apply(stability_score)
    df["age_score"] = df["launch_year"].apply(age_score)

    df["total_score"] = (
        df["tvl_score"]
        + df["stability_score"]
        + df["age_score"]
        + df["holder_concentration_score"]
        + df["audit_exploit_score"]
    )

    df["risk_level"] = df["total_score"].apply(risk_level)

    final_columns = [
        "name",
        "chain",
        "category",
        "tvl",
        "tvl_30d_change",
        "tvl_score",
        "stability_score",
        "age_score",
        "holder_concentration_score",
        "audit_exploit_score",
        "total_score",
        "risk_level",
    ]

    df = df[final_columns]
    df.to_csv(OUTPUT_PATH, index=False)

    print(df)
    print(f"\nSaved scores to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
