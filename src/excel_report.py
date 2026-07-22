import os
import pandas as pd
from utils import print_header


def generate_excel_report(
    cleaned_df,
    region_summary,
    category_summary,
    pivot_sales,
    pivot_profit,
):
    """
    Generate Excel Report
    """

    print_header("Excel Report Generation")

    os.makedirs("../reports", exist_ok=True)

    output_file = "../reports/Sales_Report.xlsx"

    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:

        cleaned_df.to_excel(
            writer,
            sheet_name="Cleaned Data",
            index=False,
        )

        region_summary.to_excel(
            writer,
            sheet_name="Region Summary",
        )

        category_summary.to_excel(
            writer,
            sheet_name="Category Summary",
        )

        pivot_sales.to_excel(
            writer,
            sheet_name="Sales Pivot",
        )

        pivot_profit.to_excel(
            writer,
            sheet_name="Profit Pivot",
        )

    print("\nExcel Report Generated Successfully!")
    print(output_file)