import plotly.express as px
import pandas as pd

# ---------------- SALES VS PROFIT ----------------
def sales_profit_chart(df):
    fig = px.bar(
        x=["Sales", "Profit"],
        y=[df["Sales"].sum(), df["Profit"].sum()],
        text=[df["Sales"].sum(), df["Profit"].sum()],
        title="💰 Total Sales vs Profit",
        color=["Sales", "Profit"]
    )
    fig.update_traces(textposition="outside")
    return fig


# ---------------- TOP CUSTOMERS ----------------
def top_customers_chart(df):
    top_customers = (
        df.groupby("Customer Name")["Sales"]
        .sum()
        .sort_values(ascending=True)
        .tail(5)
        .reset_index()
    )

    fig = px.bar(
        top_customers,
        x="Sales",
        y="Customer Name",
        orientation="h",
        title="🏆 Top 5 Customers by Sales",
        color="Sales"
    )
    return fig


# ---------------- REGION SALES ----------------
def sales_by_region_chart(df):
    region_sales = df.groupby("Region")["Sales"].sum().reset_index()

    fig = px.pie(
        region_sales,
        names="Region",
        values="Sales",
        title="🌍 Sales Distribution by Region"
    )
    return fig


# ---------------- CATEGORY PROFIT ----------------
def category_profit_chart(df):
    category_profit = df.groupby("Category")["Profit"].sum().reset_index()

    fig = px.bar(
        category_profit,
        x="Category",
        y="Profit",
        title="📦 Profit by Category",
        color="Profit"
    )
    return fig


# ---------------- MONTHLY TREND (NEW ⭐) ----------------
def monthly_sales_trend(df):

    df["Order Date"] = pd.to_datetime(df["Order Date"])

    monthly = df.groupby(
        df["Order Date"].dt.to_period("M")
    )["Sales"].sum().reset_index()

    monthly["Order Date"] = monthly["Order Date"].astype(str)

    fig = px.line(
        monthly,
        x="Order Date",
        y="Sales",
        markers=True,
        title="📈 Monthly Sales Trend"
    )

    return fig