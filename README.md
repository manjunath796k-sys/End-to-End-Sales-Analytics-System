# Capstone Sales Analytics

Project structure for the sales analytics capstone.
# 📊 End-to-End Sales Analytics Project

## Overview

The End-to-End Sales Analytics Project is developed to analyze customer sales data and generate meaningful business insights. The project covers the complete data analytics workflow including data validation, preprocessing, exploratory data analysis, visualization, SQL analysis, Excel reporting, and Power BI dashboard creation.

---

## Project Objectives

- Load customer and order datasets
- Validate and clean the data
- Merge customer and order information
- Perform exploratory data analysis (EDA)
- Generate statistical insights using NumPy
- Create visualizations using Matplotlib
- Export cleaned data and reports to Excel
- Perform SQL analysis using MySQL
- Build an interactive Power BI dashboard
- Generate business insights for decision making

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- OpenPyXL
- MySQL
- Microsoft Excel
- Power BI
- Visual Studio Code

---

## Project Structure

```
Capstone-Sales-Analytics
│
├── data
│   ├── Capstone Customers.csv
│   └── Capstone Orders.csv
│
├── src
│   ├── main.py
│   ├── loader.py
│   ├── validator.py
│   ├── preprocessing.py
│   ├── numpy_analysis.py
│   ├── eda.py
│   ├── visualization.py
│   ├── excel_report.py
│   └── utils.py
│
├── sql
│   ├── create_database.sql
│   ├── import_data.sql
│   └── analysis.sql
│
├── outputs
│   ├── cleaned_data.csv
│   ├── merged_data.csv
│   └── figures
│
├── reports
│   └── Sales_Report.xlsx
│
├── dashboard
│   └── Sales_Dashboard.pbix
│
├── notebooks
│
├── README.md
├── requirements.txt
└── LICENSE
```

---

## Project Workflow

1. Load customer and order datasets.
2. Validate datasets for missing values and duplicate records.
3. Merge datasets using CustomerID.
4. Clean and preprocess the data.
5. Perform feature engineering.
6. Analyze data using NumPy and Pandas.
7. Perform Exploratory Data Analysis (EDA).
8. Generate charts and visualizations.
9. Export cleaned data and Excel reports.
10. Perform SQL analysis.
11. Build an interactive Power BI dashboard.
12. Generate business insights.

---

## Features

- Data Validation
- Missing Value Handling
- Duplicate Removal
- Feature Engineering
- NumPy Statistical Analysis
- GroupBy Analysis
- Pivot Table Analysis
- Outlier Detection
- Correlation Analysis
- Data Visualization
- Excel Report Generation
- SQL Analysis
- Power BI Dashboard

---

## Visualizations

The project generates the following visualizations:

- Sales by Region
- Monthly Sales Trend
- Profit Distribution
- Sales vs Profit
- Correlation Heatmap

Generated charts are saved in the **outputs/figures** folder.

---

## Excel Report

The generated Excel report contains:

- Cleaned Data
- Region Summary
- Category Summary
- Sales Pivot
- Profit Pivot
- KPI Summary

---

## SQL Analysis

The SQL module includes queries for:

- Total Sales
- Total Profit
- Average Sales
- Sales by Category
- Profit by Category
- Top Customers
- Loss Making Orders
- JOIN Operations
- HAVING Clause
- CASE Statement
- Subquery
- Common Table Expression (CTE)
- Window Functions
  - RANK()
  - ROW_NUMBER()
  - DENSE_RANK()

---

## Power BI Dashboard

The dashboard includes:

- KPI Cards
- Total Sales
- Total Profit
- Total Orders
- Average Sales
- Sales by Region
- Sales by Category
- Monthly Sales Trend
- Profit by Category
- Sales vs Profit
- Region Filter
- Category Filter

---

## Business Insights

- Electronics category generated the highest sales.
- South region recorded the highest overall sales.
- Some orders generated negative profit and require attention.
- Profit margin varies across product categories.
- Sales trends help identify high-performing periods.

---

## Future Enhancements

- Sales Forecasting using Machine Learning
- Real-time Dashboard
- Database Integration
- Automated Report Generation
- Cloud Deployment

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move to the project folder:

```bash
cd Capstone-Sales-Analytics
```

Install required libraries:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
cd src
python main.py
```

---

## Output

The project generates:

- Cleaned Dataset (CSV)
- Merged Dataset (CSV)
- Excel Report
- Charts
- SQL Analysis
- Power BI Dashboard

---

## Author

Manjunath Kumbar

End-to-End Sales Analytics Project