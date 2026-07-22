from loader import load_csv
from validator import validate_data
from utils import print_header
from numpy_analysis import analyze_numpy
from preprocessing import (
    merge_datasets,
    clean_data,
    add_calculated_columns,
    save_datasets
)
from eda import (
    groupby_analysis,
    pivot_table_analysis,
    detect_outliers,
    correlation_analysis
)
from visualization import (
    sales_by_region,
    monthly_sales_trend,
    profit_distribution,
    sales_vs_profit,
    correlation_heatmap,
)
from excel_report import generate_excel_report


def main():

    print_header("End-to-End Sales Analytics System")

    # ==========================
    # File Paths
    # ==========================
    customers_file = "../data/Capstone Customers.csv"
    orders_file = "../data/Capstone Orders.csv"

    # ==========================
    # Load Data
    # ==========================
    customers_df = load_csv(customers_file)
    orders_df = load_csv(orders_file)

    # ==========================
    # Validate Data
    # ==========================
    if customers_df is not None:
        validate_data(customers_df, "Customers")

    if orders_df is not None:
        validate_data(orders_df, "Orders")

    # ==========================
    # Display Original Data
    # ==========================
    if customers_df is not None:
        print("\nCustomers Dataset")
        print(customers_df.head())
        print(f"\nShape: {customers_df.shape}")

    if orders_df is not None:
        print("\nOrders Dataset")
        print(orders_df.head())
        print(f"\nShape: {orders_df.shape}")

    # ==========================
    # NumPy Analysis
    # ==========================
    if orders_df is not None:
        analyze_numpy(orders_df)

    # ==========================
    # Merge Datasets
    # ==========================
    merged_df = merge_datasets(customers_df, orders_df)
    
    print("\nMerged Dataset")
    print(merged_df.head())
    print(f"\nMerged Shape: {merged_df.shape}")

    # ==========================
    # Clean Data
    # ==========================
    merged_df = clean_data(merged_df)

    print("\nCleaned Dataset")
    print(merged_df.head())
    print(f"\nCleaned Shape: {merged_df.shape}")

    # ==========================
    # Feature Engineering
    # ==========================
    merged_df = add_calculated_columns(merged_df)
    save_datasets(merged_df, merged_df)

    print("\nDataset with Calculated Columns")
    print(merged_df.head())
    print(f"\nShape: {merged_df.shape}")

    # ==========================
    # Exploratory Data Analysis
    # ==========================
    region_summary, category_summary = groupby_analysis(merged_df)

    pivot_sales, pivot_profit = pivot_table_analysis(merged_df)

    outliers = detect_outliers(merged_df)

    correlation = correlation_analysis(merged_df)

    # ==========================
    # Data Visualization
    # ==========================
    sales_by_region(merged_df)
    monthly_sales_trend(merged_df)
    profit_distribution(merged_df)
    sales_vs_profit(merged_df)
    correlation_heatmap(merged_df)

    # ==========================
    # Excel Report
    # ==========================

    generate_excel_report(
        merged_df,
        region_summary,
        category_summary,
        pivot_sales,
        pivot_profit,
    )

if __name__ == "__main__":
    main()