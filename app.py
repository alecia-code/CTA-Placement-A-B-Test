import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("cta_placement_test_data.csv", parse_dates=["timestamp"])

st.set_page_config(page_title="CTA Placement A/B Test", layout="wide")
st.title("🧪 CTA Placement A/B Test – Productivity App")

# Sidebar filters
with st.sidebar:
    st.header("Filter Test Results")
    variant = st.multiselect("Variant Group", df["variant_group"].unique())
    device = st.multiselect("Device Type", df["device_type"].unique())

filtered = df.copy()
if variant:
    filtered = filtered[filtered["variant_group"].isin(variant)]
if device:
    filtered = filtered[filtered["device_type"].isin(device)]

# KPI Cards
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Sessions", f"{filtered.shape[0]:,}")
col2.metric("CTR", f"{filtered['cta_clicked'].mean()*100:.2f}%" if filtered.shape[0] else "0%")
col3.metric("Conversion Rate", f"{filtered['converted'].mean()*100:.2f}%" if filtered.shape[0] else "0%")
col4.metric("Revenue / Session", f"${filtered['revenue'].mean():.2f}")
col5.metric("Avg Scroll Depth", f"{filtered['scroll_depth_pct'].mean()*100:.1f}%")

# CTR by Variant
st.subheader("📊 Click-Through Rate by Variant")
ctr_variant = df.groupby("variant_group")["cta_clicked"].mean().reset_index()
ctr_fig = px.bar(ctr_variant, x="variant_group", y="cta_clicked",
                 labels={"cta_clicked": "CTR"}, title="CTR by Variant")
st.plotly_chart(ctr_fig, use_container_width=True)

# Conversion by Variant & Device
st.subheader("📈 Conversion Rate by Variant & Device")
conversion_fig = px.bar(df.groupby(["variant_group", "device_type"])["converted"].mean().reset_index(),
                        x="variant_group", y="converted", color="device_type", barmode="group",
                        labels={"converted": "Conversion Rate"}, title="Conversion by Variant & Device")
st.plotly_chart(conversion_fig, use_container_width=True)

# Revenue by Group
st.subheader("💰 Revenue Per Session by Variant")
revenue_fig = px.box(df, x="variant_group", y="revenue", color="variant_group",
                     title="Revenue Distribution by Variant")
st.plotly_chart(revenue_fig, use_container_width=True)

# Engagement Breakdown
st.subheader("🧭 Scroll Depth vs Session Duration")
engagement_fig = px.scatter(filtered, x="scroll_depth_pct", y="session_duration_sec",
                            color="variant_group", size="revenue", opacity=0.6,
                            title="Engagement by Scroll Depth and Session Duration",
                            labels={"scroll_depth_pct": "Scroll Depth (%)", "session_duration_sec": "Session Duration (sec)"})
st.plotly_chart(engagement_fig, use_container_width=True)