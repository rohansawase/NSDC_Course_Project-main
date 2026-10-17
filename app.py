
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------
# 1. Page configuration
# ---------------------------------
st.set_page_config(
    page_title="Retail Sales Analytics",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------
# 2. Dashboard title
# ---------------------------------
st.title("📊 Retail Sales Analytics Dashboard")
st.write(
    "Explore historical retail sales through "
    "interactive metrics, charts, and country analysis."
)

# ---------------------------------
# 3. Load cleaned data
# ---------------------------------
@st.cache_data
def load_data():
    data = pd.read_csv("retail_sales_cleaned.csv")
    data["InvoiceDate"] = pd.to_datetime(data["InvoiceDate"])
    data["YearMonth"] = data["InvoiceDate"].dt.to_period("M")
    return data

try:
    df_clean = load_data()
except FileNotFoundError:
    st.error(
        "Dataset not found. Place retail_sales_cleaned.csv "
        "in the same folder as app.py."
    )
    st.stop()

# ---------------------------------
# 4. Calculate key metrics
# ---------------------------------
total_revenue = df_clean["Revenue"].sum()
total_units = df_clean["Quantity"].sum()
total_invoices = df_clean["InvoiceNo"].nunique()
total_countries = df_clean["Country"].nunique()

# ---------------------------------
# 5. Display KPI cards
# ---------------------------------
st.subheader("Business Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"£{total_revenue:,.2f}")
col2.metric("Units Sold", f"{total_units:,.0f}")
col3.metric("Unique Invoices", f"{total_invoices:,}")
col4.metric("Countries", f"{total_countries}")

st.divider()

# ---------------------------------
# 6. Monthly revenue trend
# ---------------------------------
st.subheader("Monthly Revenue Trend")

monthly_revenue = (
    df_clean.groupby("YearMonth")["Revenue"]
    .sum()
)

fig1, ax1 = plt.subplots(figsize=(12, 5))

monthly_revenue.plot(
    kind="line",
    figsize=(12, 5),
    marker="o",
    ax=ax1
)

ax1.set_title("Monthly Revenue Trend")
ax1.set_xlabel("Month")
ax1.set_ylabel("Revenue (£)")
ax1.tick_params(axis="x", rotation=45)
ax1.grid(True, alpha=0.3)

fig1.tight_layout()
st.pyplot(fig1)
plt.close(fig1)

# ---------------------------------
# 7. Top 10 products by revenue
# ---------------------------------
st.subheader("Top 10 Products by Revenue")

non_product_descriptions = [
    "DOTCOM POSTAGE",
    "POSTAGE",
    "Manual"
]

product_sales = df_clean[
    ~df_clean["Description"].isin(non_product_descriptions)
]

top_products = (
    product_sales.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig2, ax2 = plt.subplots(figsize=(10, 6))

top_products.sort_values().plot(
    kind="barh",
    ax=ax2
)

ax2.set_title("Top 10 Products by Revenue")
ax2.set_xlabel("Revenue (£)")
ax2.set_ylabel("Product")

fig2.tight_layout()
st.pyplot(fig2)
plt.close(fig2)

# ---------------------------------
# 8. Top 10 countries by revenue
# ---------------------------------
st.subheader("Top 10 Countries by Revenue")

country_revenue = (
    df_clean.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

top_countries = country_revenue.head(10)

fig3, ax3 = plt.subplots(figsize=(10, 6))

top_countries.sort_values().plot(
    kind="barh",
    ax=ax3
)

ax3.set_title("Top 10 Countries by Revenue")
ax3.set_xlabel("Revenue (£)")
ax3.set_ylabel("Country")

fig3.tight_layout()
st.pyplot(fig3)
plt.close(fig3)

# ---------------------------------
# 9. Dataset preview
# ---------------------------------
with st.expander("View cleaned dataset"):
    st.dataframe(df_clean.head(100), use_container_width=True)

# ---------------------------------
# 10. Project note
# ---------------------------------
st.caption(
    "Dataset: UCI Online Retail historical transactions, "
    "December 2010–December 2011. "
    "Revenue is calculated as Quantity × UnitPrice in GBP. "
    "Cancelled invoices, bad-debt adjustments, missing "
    "descriptions, and non-positive unit prices were excluded "
    "during cleaning. These results describe the filtered dataset, "
    "not profit or the retailer's complete reported revenue."
)
