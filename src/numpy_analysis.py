import numpy as np
from utils import print_header


def analyze_numpy(df):

    print_header("NumPy Analysis")

    # Convert to NumPy Arrays
    sales = df["Sales"].dropna().to_numpy()
    profit = df["Profit"].dropna().to_numpy()

    print(f"Sales Array Size : {sales.size}")
    print(f"Profit Array Size: {profit.size}")

    print("\n----- Sales Statistics -----")
    print(f"Mean               : {np.mean(sales):.2f}")
    print(f"Standard Deviation : {np.std(sales):.2f}")
    print(f"Minimum Sales      : {np.min(sales):.2f}")
    print(f"Maximum Sales      : {np.max(sales):.2f}")

    print("\n----- Profit Statistics -----")
    print(f"Mean               : {np.mean(profit):.2f}")
    print(f"Standard Deviation : {np.std(profit):.2f}")
    print(f"Minimum Profit     : {np.min(profit):.2f}")
    print(f"Maximum Profit     : {np.max(profit):.2f}")

    # Normalize Sales
    normalized_sales = (sales - np.min(sales)) / (np.max(sales) - np.min(sales))

    print("\nFirst 10 Normalized Sales Values")
    for i, value in enumerate(normalized_sales[:10], start=1):
        print(f"{i}. {value:.4f}")

    # Loss Making Orders

    loss_orders = df[df["Profit"] < 0]

    print(f"\nTotal Loss Making Orders : {len(loss_orders)}")

    print("\nFirst 10 Loss Making Orders")
    print(loss_orders[["OrderID", "CustomerID", "Category", "Sales", "Profit"]].head(10))