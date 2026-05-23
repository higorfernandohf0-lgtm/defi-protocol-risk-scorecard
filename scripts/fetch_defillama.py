import requests
import pandas as pd
from pathlib import Path

BASE_URL = "https://api.llama.fi"

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "protocols.csv"
OUTPUT_PATH = ROOT / "data" / "defillama_raw.csv"


def get_protocol_data(slug):
    url = f"{BASE_URL}/protocol/{slug}"

    response = requests.get(url, timeout=30)

    response.raise_for_status()

    return response.json()


def calculate_30d_change(tvl_history):

    if not tvl_history or len(tvl_history) < 30:
        return None

    current_tvl = tvl_history[-1].get("totalLiquidityUSD", 0)

    tvl_30d_ago = tvl_history[-30].get("totalLiquidityUSD", 0)

    if tvl_30d_ago == 0:
        return None

    return ((current_tvl - tvl_30d_ago) / tvl_30d_ago) * 100


def main():

    protocols = pd.read_csv(CONFIG_PATH)

    rows = []

    for _, row in protocols.iterrows():

        name = row["name"]
        slug = row["slug"]

        print(f"Fetching {name}...")

        try:

            data = get_protocol_data(slug)

            tvl_history = data.get("tvl", [])

            current_tvl = (
                tvl_history[-1].get("totalLiquidityUSD", 0)
                if tvl_history
                else 0
            )

            tvl_30d_change = calculate_30d_change(tvl_history)

            rows.append({
                "name": name,
                "slug": slug,
                "chain": row["chain"],
                "category": row["category"],
                "launch_year": row["launch_year"],
                "holder_concentration_score": row["holder_concentration_score"],
                "audit_exploit_score": row["audit_exploit_score"],
                "tvl": round(current_tvl, 2),
                "tvl_30d_change": (
                    round(tvl_30d_change, 2)
                    if tvl_30d_change is not None
                    else None
                ),
            })

        except Exception as e:
            print(f"Error fetching {name}: {e}")

    df = pd.DataFrame(rows)

    df.to_csv(OUTPUT_PATH, index=False)

    print("\nSaved raw data successfully.")


if __name__ == "__main__":
    main()