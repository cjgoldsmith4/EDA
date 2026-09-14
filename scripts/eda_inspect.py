"""
EDA inspection script for wildcat_loans_clean.csv.

Loads the dataset into a pandas DataFrame and prints:
  - shape (rows, columns)
  - all column names with their data types
  - count of missing values per column
"""

import pandas as pd

DATA_PATH = "02_Data/Raw/wildcat_loans_clean.csv"


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


if __name__ == "__main__":
    main()
