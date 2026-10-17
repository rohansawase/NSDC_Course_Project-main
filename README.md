# 📊 Retail Sales Data Analytics Using Python

**NSDC Certification Course Project**

A data analytics project that uses Python to clean, analyze, and visualize historical retail transaction data through an interactive Streamlit dashboard.

## 👥 Project Team

- **Vijay**
- **Rohan**
- **Nikhil**

## 📌 Project Overview

Retail businesses generate large amounts of transaction data every day. Analyzing this data can help businesses understand their sales performance, identify high-revenue products, monitor monthly trends, and discover which countries contribute most to revenue.

This project demonstrates how Python and data analytics techniques can transform raw retail transaction data into meaningful business insights using Exploratory Data Analysis (EDA) and interactive visualizations.

## ❓ Problem Statement

Retail transaction datasets contain thousands of records, making it difficult to understand business performance by manually examining individual transactions.

Without proper data cleaning and analysis, it can be challenging to answer important business questions, such as:

- What is the total recorded sales revenue?
- Which products generate the highest revenue?
- How does revenue change from month to month?
- Which countries contribute the most revenue?
- How can raw transaction data be transformed into useful business insights?

## 🎯 Project Objectives

- Clean and prepare raw retail transaction data for analysis.
- Identify missing values and duplicate records.
- Handle cancellation-related invoices and invalid sales records.
- Calculate transaction-level revenue.
- Perform Exploratory Data Analysis (EDA).
- Identify the top 10 products and countries by revenue.
- Analyze monthly revenue trends.
- Develop an interactive dashboard using Streamlit.
- Present the results through clear charts and key performance indicators (KPIs).

## 📂 Dataset Source

**Dataset:** Online Retail

**Source:** UCI Machine Learning Repository

**Official dataset page:**  
https://archive.ics.uci.edu/dataset/352/online+retail

The dataset contains historical transactions from a UK-based, non-store online retailer between **1 December 2010 and 9 December 2011**.

The original dataset contains 541,909 transaction records and eight columns.

### Dataset Columns

| Column | Description |
|---|---|
| InvoiceNo | Transaction or invoice identifier |
| StockCode | Product code |
| Description | Product description |
| Quantity | Number of units in a transaction |
| InvoiceDate | Date and time of the transaction |
| UnitPrice | Price per unit in GBP |
| CustomerID | Customer identifier |
| Country | Country associated with the transaction |

The dataset is used for educational and analytical purposes. It represents historical transactions, not live sales data from a current business.

## 🛠️ Technologies Used

- **Python** — Core programming language
- **Pandas** — Data manipulation and analysis
- **NumPy** — Numerical computing
- **Matplotlib** — Data visualization
- **Jupyter Notebook** — Data cleaning, analysis, and experimentation
- **Streamlit** — Interactive web dashboard
- **Git and GitHub** — Version control and project hosting

## 🔄 Project Workflow

### 1. Data Collection

Downloaded the Online Retail dataset from the UCI Machine Learning Repository.

### 2. Data Exploration

Examined the dataset structure, column data types, missing values, duplicate records, transaction dates, and sales-related anomalies.

### 3. Data Cleaning and Preprocessing

The following cleaning steps were performed:

- Removed 5,268 duplicate records.
- Excluded cancellation-related invoices identified by invoice numbers beginning with `C`.
- Excluded bad-debt adjustment records.
- Excluded records with missing product descriptions.
- Excluded records with zero or negative unit prices for the main sales analysis.
- Prepared a cleaned dataset for further analysis.

After these filtering steps, the working dataset contained **524,877 transaction rows**.

These choices define the scope of this project's sales analysis. The resulting figures should not be interpreted as the retailer's complete officially reported revenue.

### 4. Revenue Calculation

Revenue was calculated for each transaction row using:

`Revenue = Quantity × UnitPrice`

All monetary values are expressed in British pounds (GBP).

Revenue is not the same as profit because the dataset does not provide the complete costs required to calculate profit.

### 5. Exploratory Data Analysis

The following analyses were performed:

- Overall sales performance
- Top 10 products by revenue
- Monthly revenue trends
- Top 10 countries by revenue

### 6. Interactive Dashboard

A Streamlit application was developed to display the key metrics and visualizations in a single interface.

## 📈 Key Findings

The following results were obtained from the cleaned dataset used in this project.

### Overall Metrics

| Metric | Result |
|---|---:|
| Total recorded revenue | £10,631,048.74 |
| Total units sold | 5,572,419 |
| Unique invoices | 19,959 |
| Unique product codes | 3,921 |
| Countries represented | 38 |

### Top Products by Revenue

The highest-revenue products included:

1. Regency Cakestand 3 Tier
2. Paper Craft, Little Birdie
3. White Hanging Heart T-Light Holder
4. Party Bunting
5. Jumbo Bag Red Retrospot

Postage and manual adjustment entries were excluded from the separate product-ranking analysis.

### Monthly Revenue Trend

The analysis showed that recorded revenue increased significantly during September, October, and November 2011, reaching its highest monthly value in November.

December 2011 contains transactions only through 9 December, so its value should not be compared directly with a complete month.

### Revenue by Country

The United Kingdom generated the highest recorded revenue in the cleaned dataset, followed by the Netherlands and EIRE (Ireland).

These findings describe the analyzed historical data and do not establish the causes of changes in revenue.

## 🖥️ Dashboard Features

The Streamlit dashboard includes:

- Four KPI cards for total revenue, units sold, unique invoices, and countries
- Monthly revenue trend line chart
- Top 10 products by revenue horizontal bar chart
- Top 10 countries by revenue horizontal bar chart
- A dataset preview for inspecting cleaned records

## 📁 Project Structure

```text
NSDC_Course_Project/
│
├── app.py
├── retail_sales_analysis.ipynb
├── retail_sales_cleaned.csv
├── requirements.txt
├── README.md
└── .gitignore
```

The original Excel dataset is maintained separately and is not included in this example structure.

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or a compatible Python version
- Git
- A code editor such as Visual Studio Code

### Step 1: Clone the repository

```bash
git clone https://github.com/Vijay96k/NSDC_Course_Project.git
```

### Step 2: Open the project directory

```bash
cd NSDC_Course_Project
```

### Step 3: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Run the Streamlit dashboard

```bash
python -m streamlit run app.py
```

The dashboard should open in your default web browser. If it does not, open the local URL shown in the terminal, usually `http://localhost:8501`.

### Running the Jupyter Notebook

Open `retail_sales_analysis.ipynb` in Jupyter Notebook or VS Code.

To reproduce the original data-loading and cleaning workflow, obtain the original Excel dataset from the UCI source and place it in the location expected by the notebook.

## 💡 Limitations

- The dataset contains historical transactions and does not provide real-time business information.
- The analysis uses a filtered dataset, so its revenue totals may differ from totals calculated under other accounting or data-cleaning rules.
- Profit, operating costs, and profit margins cannot be calculated reliably from the available columns.
- December 2011 is an incomplete month in the supplied data.
- The product ranking excludes selected postage and manual entries, but other unusual product descriptions may still require further investigation.

## 🚀 Future Improvements

- Add interactive filters for date, country, and product.
- Include quantity-based product rankings.
- Compare revenue across selected periods.
- Add downloadable reports.
- Improve the dashboard layout and chart formatting.
- Deploy the dashboard online for easier access.
- Add additional business insights and more detailed customer analysis.

## 🎓 Conclusion

This project demonstrates a practical data analytics workflow, from collecting and cleaning raw transaction data to performing exploratory analysis and developing an interactive dashboard.

By using Python, Pandas, Matplotlib, Jupyter Notebook, and Streamlit, the project converts historical retail transactions into visual insights that are easier to understand and communicate.

**Project created as part of the NSDC Certification Course.**

---

**Team Members:** Vijay | Rohan | Nikhil
