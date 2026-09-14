"""
EDA inspection script for wildcat_loans_clean.csv.

Loads the dataset into a pandas DataFrame and prints:
  - shape (rows, columns)
  - all column names with their data types
  - count of missing values per column
  - a check (and conversion, if needed) of origination_date to datetime
"""

from pathlib import Path

import pandas as pd

# Resolved relative to this script's location so it works regardless of
# the working directory VS Code (or anything else) runs it from.
DATA_PATH = Path(__file__).resolve().parent.parent / "02_Data" / "Raw" / "wildcat_loans_clean.csv"


def main():
    df = pd.read_csv(DATA_PATH)

    print("=" * 60)
    print("SHAPE")
    print("=" * 60)
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print()
    print("=" * 60)
    print("COLUMN NAMES AND DATA TYPES")
    print("=" * 60)
    print(df.dtypes)

    print()
    print("=" * 60)
    print("MISSING VALUES PER COLUMN")
    print("=" * 60)
    print(df.isnull().sum())

    print()
    print("=" * 60)
    print("ORIGINATION_DATE TYPE CHECK")
    print("=" * 60)
    before_type = df["origination_date"].dtype
    print(f"Before: {before_type}")

    if pd.api.types.is_datetime64_any_dtype(df["origination_date"]):
        print("Already stored as datetime — no conversion needed.")
    else:
        df["origination_date"] = pd.to_datetime(df["origination_date"])
        after_type = df["origination_date"].dtype
        print(f"Was stored as text (object) — converted to datetime.")
        print(f"After: {after_type}")


if __name__ == "__main__":
    main()
