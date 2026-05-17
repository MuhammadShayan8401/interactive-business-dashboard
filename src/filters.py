import streamlit as st
import pandas as pd


def apply_filters(df):

    st.sidebar.header("🔍 Filters")

    # Ensure datetime
    df["Order Date"] = pd.to_datetime(df["Order Date"])

    # ---------------- DATE FILTER ----------------
    min_date = df["Order Date"].min()
    max_date = df["Order Date"].max()

    date_range = st.sidebar.date_input(
        "Select Date Range",
        [min_date, max_date]
    )

    if len(date_range) == 2:
        start_date, end_date = date_range
        df = df[
            (df["Order Date"] >= pd.to_datetime(start_date)) &
            (df["Order Date"] <= pd.to_datetime(end_date))
        ]

    # ---------------- REGION ----------------
    region = st.sidebar.multiselect(
        "Region",
        options=df["Region"].unique(),
        default=df["Region"].unique()
    )

    # ---------------- CATEGORY ----------------
    category = st.sidebar.multiselect(
        "Category",
        options=df["Category"].unique(),
        default=df["Category"].unique()
    )

    # ---------------- SUB-CATEGORY ----------------
    sub_category = st.sidebar.multiselect(
        "Sub-Category",
        options=df["Sub-Category"].unique(),
        default=df["Sub-Category"].unique()
    )

    # ---------------- APPLY FILTERS ----------------
    filtered_df = df[
        (df["Region"].isin(region)) &
        (df["Category"].isin(category)) &
        (df["Sub-Category"].isin(sub_category))
    ]

    return filtered_df