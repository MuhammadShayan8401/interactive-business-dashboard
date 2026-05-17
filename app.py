import streamlit as st
from src.data_loader import load_data
from src.preprocessing import clean_data
from src.filters import apply_filters
from src.metrics import calculate_kpis
from src.charts import (
    sales_profit_chart,
    top_customers_chart,
    sales_by_region_chart,
    category_profit_chart,
    monthly_sales_trend
)

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Global Superstore Dashboard",
    layout="wide",
    page_icon="📊"
)

# ---------------- CUSTOM UI STYLE ----------------
st.markdown("""
<style>
section[data-testid="stSidebar"] {
    background-color: #111827;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.title("📊 Global Superstore BI Dashboard")
st.markdown("### Interactive Sales, Profit & Customer Analytics")

st.divider()

# ---------------- LOAD DATA ----------------
df = load_data()
df = clean_data(df)

# ---------------- FILTERS ----------------
filtered_df = apply_filters(df)

# ---------------- KPIs ----------------
total_sales, total_profit, total_orders, top_customers = calculate_kpis(filtered_df)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("💰 Total Sales", f"${total_sales:,.0f}")

with col2:
    st.metric("📈 Total Profit", f"${total_profit:,.0f}")

with col3:
    st.metric("🧾 Total Orders", f"{total_orders}")

st.divider()

# ---------------- CHARTS ----------------
st.subheader("📊 Business Insights")

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(sales_profit_chart(filtered_df), use_container_width=True)

with col2:
    st.plotly_chart(top_customers_chart(filtered_df), use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    st.plotly_chart(sales_by_region_chart(filtered_df), use_container_width=True)

with col4:
    st.plotly_chart(category_profit_chart(filtered_df), use_container_width=True)

# ---------------- TREND CHART ----------------
st.divider()

st.plotly_chart(monthly_sales_trend(filtered_df), use_container_width=True)

# ---------------- DATA PREVIEW ----------------
st.divider()

st.subheader("📄 Filtered Dataset")
st.dataframe(filtered_df, use_container_width=True)