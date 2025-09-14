import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="📊 Marketing & Business Dashboard", layout="wide")

# Load Data 
DATA_DIR = "data"

@st.cache_data
def load_data():
    marketing_files = ["Facebook.csv", "Google.csv", "TikTok.csv"]
    marketing_data = {}
    for f in marketing_files:
        path = os.path.join(DATA_DIR, f)
        if os.path.exists(path):
            df = pd.read_csv(path)
            df["date"] = pd.to_datetime(df["date"])
            df["source"] = f.replace(".csv", "")
            marketing_data[f.replace(".csv", "")] = df

    business = None
    business_path = os.path.join(DATA_DIR, "Business.csv")
    if os.path.exists(business_path):
        business = pd.read_csv(business_path)
        business["date"] = pd.to_datetime(business["date"])

    return marketing_data, business

marketing_data_raw, business_data_raw = load_data()


st.sidebar.header("Data Selection")
view = st.sidebar.radio("Choose View", ["Marketing", "Business"])
platform = st.sidebar.selectbox("Select Platform", list(marketing_data_raw.keys()))


min_date = business_data_raw["date"].min()
max_date = business_data_raw["date"].max()

start_date = st.sidebar.date_input("Start Date", min_value=min_date, max_value=max_date, value=min_date)
end_date = st.sidebar.date_input("End Date", min_value=min_date, max_value=max_date, value=max_date)

# Ensure end_date >= start_date
if end_date < start_date:
    st.sidebar.error("End Date must be after or equal to Start Date")
    end_date = start_date

start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)


marketing_data = {
    platform_name: df[(df["date"] >= start_date) & (df["date"] <= end_date)]
    for platform_name, df in marketing_data_raw.items()
}

business_data = business_data_raw[(business_data_raw["date"] >= start_date) & 
                                  (business_data_raw["date"] <= end_date)]


available_metrics = [col for col in ["# of orders", "# of new orders", "new customers"] 
                     if col in business_data.columns]

if available_metrics:
    df_orders = business_data.melt(
        id_vars="date",
        value_vars=available_metrics,
        var_name="Metric",
        value_name="Count"
    )





#                                                        Marketing Dashboard 
if view == "Marketing":
    st.title("📈 Marketing Campaign Dashboard")

    df = marketing_data[platform]

   
    total_spend = df['spend'].sum()
    total_revenue = df['attributed revenue'].sum()
    total_impressions = df['impression'].sum()
    total_clicks = df['clicks'].sum()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("💰 Total Spend", f"${total_spend:,.0f}")
    col2.metric("📈 Total Revenue (Attributed)", f"${total_revenue:,.0f}")
    col3.metric("👀 Total Impressions", f"{total_impressions:,.0f}")
    col4.metric("🖱 Total Clicks", f"{total_clicks:,.0f}")

    st.subheader(f"{platform} Campaign Data")
    st.dataframe(df.head())

   # Spend vs Time
    fig = px.line(df, x="date", y="spend", color="campaign",
                    title=f"{platform} - Spend Over Time")
    st.plotly_chart(fig, use_container_width=True)

   #Revenue vs Time
    fig = px.line(df, x="date", y="attributed revenue", color="campaign",
                    title=f"{platform} - Revenue Over Time")
    st.plotly_chart(fig, use_container_width=True)

    # Impressions vs Clicks 
    fig = px.scatter(df, x="impression", y="clicks", color="campaign",
                     size="spend", hover_data=["state"],
                     title=f"{platform} - Impressions vs Clicks")
    st.plotly_chart(fig, use_container_width=True)




#                                                                     Business Dashboard 
elif view == "Business":
    st.title("🏬 Business Performance Dashboard")

    if business_data is not None and not business_data.empty:
        total_revenue = business_data['total revenue'].sum()
        total_orders = business_data['# of orders'].sum() if '# of orders' in business_data.columns else 0
        new_customers = business_data['new customers'].sum() if 'new customers' in business_data.columns else 0

        col1, col2, col3 = st.columns(3)
        col1.metric("📈 Total Revenue", f"${total_revenue:,.0f}")
        col2.metric("🛒 Total Orders", f"{total_orders:,}")
        col3.metric("👤 New Customers", f"{new_customers:,}")

        st.subheader("Daily Business Data")
        st.dataframe(business_data.head())

        # Revenue trend
        fig = px.line(business_data, x="date", y="total revenue",
                      title="Total Revenue Over Time")
        st.plotly_chart(fig, use_container_width=True)

        # Orders vs New Customers
        if available_metrics:
            fig = px.bar(df_orders, x="date", y="Count", color="Metric",
                         barmode="group", title="Orders & New Customers Over Time")
            st.plotly_chart(fig, use_container_width=True)

        # Show Profit 
        profit_cols = [col for col in ["gross profit", "COGS"] if col in business_data.columns]
        if profit_cols:
            fig = px.area(business_data, x="date", y=profit_cols,
                          title="Profit vs COGS Over Time")
            st.plotly_chart(fig, use_container_width=True)

    else:
        st.error("No business data available for the selected date range.")


