import os
import pandas as pd
from utils import print_header


def merge_datasets(customers_df, orders_df):
    """
    Merge Customers and Orders using CustomerID.
    """

    print_header("Merging Datasets")

    # Check duplicate Customer IDs
    duplicate_customer_ids = customers_df["CustomerID"].value_counts()
    duplicate_customer_ids = duplicate_customer_ids[duplicate_customer_ids > 1]

    if not duplicate_customer_ids.empty:
        print("\nDuplicate Customer IDs Found:")
        print(duplicate_customer_ids)

        # Remove duplicate customer records
        customers_df = customers_df.drop_duplicates(
            subset="CustomerID",
            keep="first"
        )

        print("\nDuplicate customer records removed.")

    else:
        print("\nNo duplicate Customer IDs found.")

    # Merge datasets
    merged_df = pd.merge(
        orders_df,
        customers_df,
        on="CustomerID",
        how="left"
    )

    print("\nMerge Completed Successfully.")
    print(f"Rows    : {merged_df.shape[0]}")
    print(f"Columns : {merged_df.shape[1]}")

    return merged_df


def clean_data(df):
    """
    Handle missing values, standardize text,
    and remove duplicate records.
    """

    print_header("Cleaning Dataset")

    print("\nMissing Values Before Cleaning:")
    print(df.isnull().sum())

    # Fill missing categorical values
    df["Region"] = df["Region"].fillna("Unknown")
    df["Segment"] = df["Segment"].fillna("Unknown")
    df["CustomerName"] = df["CustomerName"].fillna("Unknown Customer")
    df["JoinDate"] = df["JoinDate"].fillna("Not Available")

    # Fill missing numerical values
    df["Sales"] = df["Sales"].fillna(df["Sales"].median())
    df["Profit"] = df["Profit"].fillna(df["Profit"].median())

    # Standardize text columns
    df["Region"] = df["Region"].str.strip().str.title()
    df["Segment"] = df["Segment"].str.strip().str.title()
    df["Category"] = df["Category"].str.strip().str.title()

    # Remove duplicate rows
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)

    print(f"\nDuplicate Rows Removed: {before - after}")

    print("\nMissing Values After Cleaning:")
    print(df.isnull().sum())

    print("\nDataset Shape After Cleaning:")
    print(df.shape)

    return df


def add_calculated_columns(df):
    """
    Add calculated columns to the dataset.
    """

    print_header("Feature Engineering")

    # Profit Margin (%)
    df["Profit Margin"] = (df["Profit"] / df["Sales"]) * 100

    # Profit Per Unit
    df["Profit Per Unit"] = df["Profit"] / df["Quantity"]

    print("\nCalculated Columns Added Successfully.")

    print("\nNew Columns:")
    print(df[["Profit Margin", "Profit Per Unit"]].head())

    print(f"\nTotal Columns: {df.shape[1]}")

    return df


    import os


def save_datasets(merged_df, cleaned_df):
    """
    Save merged and cleaned datasets as CSV files.
    """

    os.makedirs("../outputs", exist_ok=True)

    merged_df.to_csv(
        "../outputs/merged_data.csv",
        index=False
    )

    cleaned_df.to_csv(
        "../outputs/cleaned_data.csv",
        index=False
    )

    print("\nDatasets saved successfully.")
    print("Merged Dataset  : ../outputs/merged_data.csv")
    print("Cleaned Dataset : ../outputs/cleaned_data.csv")