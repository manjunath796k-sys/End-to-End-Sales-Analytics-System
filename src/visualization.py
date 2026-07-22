import os
import matplotlib.pyplot as plt
import pandas as pd

from utils import print_header

# Create output folder
os.makedirs("../outputs/figures", exist_ok=True)


def sales_by_region(df):
    print_header("Sales by Region")

    sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    sales.plot(kind="bar")

    plt.title("Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Total Sales")

    plt.tight_layout()

    plt.savefig("../outputs/figures/sales_by_region.png", dpi=300)
    plt.show()
    plt.close()


def monthly_sales_trend(df):
    print_header("Monthly Sales Trend")

    df["OrderDate"] = pd.to_datetime(df["OrderDate"])

    monthly_sales = (
        df.groupby(df["OrderDate"].dt.to_period("M"))["Sales"]
        .sum()
    )

    monthly_sales.index = monthly_sales.index.astype(str)

    plt.figure(figsize=(12, 6))

    monthly_sales.plot(marker="o")

    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("../outputs/figures/monthly_sales.png", dpi=300)

    plt.show()
    plt.close()


def profit_distribution(df):
    print_header("Profit Distribution")

    plt.figure(figsize=(10, 6))

    plt.hist(df["Profit"], bins=20)

    plt.title("Profit Distribution")
    plt.xlabel("Profit")
    plt.ylabel("Frequency")

    plt.tight_layout()

    plt.savefig("../outputs/figures/profit_distribution.png", dpi=300)

    plt.show()
    plt.close()


def sales_vs_profit(df):
    print_header("Sales vs Profit")

    plt.figure(figsize=(8, 6))

    plt.scatter(df["Sales"], df["Profit"])

    plt.title("Sales vs Profit")
    plt.xlabel("Sales")
    plt.ylabel("Profit")

    plt.tight_layout()

    plt.savefig("../outputs/figures/sales_vs_profit.png", dpi=300)

    plt.show()
    plt.close()


def correlation_heatmap(df):
    print_header("Correlation Heatmap")

    correlation = df[
        [
            "Sales",
            "Profit",
            "Quantity",
            "Discount",
            "Profit Margin",
            "Profit Per Unit",
        ]
    ].corr()

    plt.figure(figsize=(8, 6))

    plt.imshow(correlation)

    plt.colorbar()

    plt.xticks(
        range(len(correlation.columns)),
        correlation.columns,
        rotation=45,
    )

    plt.yticks(
        range(len(correlation.columns)),
        correlation.columns,
    )

    plt.title("Correlation Heatmap")

    plt.tight_layout()

    plt.savefig("../outputs/figures/correlation_heatmap.png", dpi=300)

    plt.show()
    plt.close()
    