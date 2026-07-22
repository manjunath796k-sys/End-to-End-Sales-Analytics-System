import pandas as pd
from utils import print_header


def groupby_analysis(df):
    """
    Perform GroupBy analysis with multiple aggregations.
    """

    print_header("GroupBy Analysis")

    # Sales by Region
    region_summary = df.groupby("Region").agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Average_Sales=("Sales", "mean"),
        Total_Orders=("OrderID", "count")
    )

    print("\nSales by Region")
    print(region_summary)

    # Sales by Category
    category_summary = df.groupby("Category").agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Average_Profit=("Profit", "mean"),
        Total_Orders=("OrderID", "count")
    )

    print("\nSales by Category")
    print(category_summary)

    return region_summary, category_summary

def pivot_table_analysis(df):
    """
    Create Pivot Tables.
    """

    print_header("Pivot Table Analysis")

    # Pivot Table: Sales by Region and Category
    pivot_sales = pd.pivot_table(
        df,
        values="Sales",
        index="Region",
        columns="Category",
        aggfunc="sum",
        fill_value=0
    )

    print("\nSales Pivot Table (Region vs Category)")
    print(pivot_sales)

    # Pivot Table: Profit by Region and Category
    pivot_profit = pd.pivot_table(
        df,
        values="Profit",
        index="Region",
        columns="Category",
        aggfunc="sum",
        fill_value=0
    )

    print("\nProfit Pivot Table (Region vs Category)")
    print(pivot_profit)

    return pivot_sales, pivot_profit


def detect_outliers(df):
    """
    Detect outliers using the IQR method.
    """

    print_header("Outlier Detection")

    Q1 = df["Sales"].quantile(0.25)
    Q3 = df["Sales"].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - (1.5 * IQR)
    upper_bound = Q3 + (1.5 * IQR)

    outliers = df[
        (df["Sales"] < lower_bound) |
        (df["Sales"] > upper_bound)
    ]

    print(f"\nLower Bound : {lower_bound:.2f}")
    print(f"Upper Bound : {upper_bound:.2f}")

    print(f"\nTotal Outliers : {len(outliers)}")

    print("\nFirst 10 Outliers")
    print(
        outliers[
            ["OrderID", "Category", "Sales", "Profit"]
        ].head(10)
    )

    return outliers


def correlation_analysis(df):
    """
    Generate a correlation matrix.
    """

    print_header("Correlation Matrix")

    correlation = df[
        [
            "Sales",
            "Profit",
            "Quantity",
            "Discount",
            "Profit Margin",
            "Profit Per Unit"
        ]
    ].corr()

    print(correlation)

    return correlation