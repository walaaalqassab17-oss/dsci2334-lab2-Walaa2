import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Admissions Explorer", page_icon="🎓")
st.title("🎓 Graduate Admissions Explorer")
st.write("Explore how test scores and CGPA relate to the chance of admission.")


@st.cache_data
def load_data():
    df = pd.read_csv("Admission_Predict_Ver1.1.csv")
    df.columns = df.columns.str.strip()  # some column names end with a space
    return df


df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
min_cgpa = st.sidebar.slider("Minimum CGPA", 6.5, 10.0, 9.0, 0.1)
research = st.sidebar.selectbox("Research experience", ["All", "Yes", "No"])

view = df[df["CGPA"] >= min_cgpa]
if research != "All":
    view = view[view["Research"] == (1 if research == "Yes" else 0)]

# Key numbers

else:
    st.warning("No students match these filters. Lower the minimum CGPA.")

# Chart
fig, ax = plt.subplots()
ax.scatter(view["GRE Score"], view["Chance of Admit"], alpha=0.6)
ax.set_xlabel("GRE Score")
ax.set_ylabel("Chance of Admit")
ax.set_title("GRE Score vs Chance of Admit")
st.pyplot(fig)

# Data table
st.subheader("First 20 matching students")
st.dataframe(view.head(20))
ax2.set_ylabel("Number of students")
st.pyplot(fig2)











import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Qahwa Corner Dashboard",
    page_icon="☕",
    layout="wide"
)

st.title("☕ Qahwa Corner Sales Dashboard")
st.write("Coffee Shop Sales Analysis - January to June 2026")

# Load dataset
df = pd.read_csv("cafe_sales.csv")
df["date"] = pd.to_datetime(df["date"])

# Branch selector
branches = ["All Branches"] + sorted(df["branch"].unique().tolist())
selected_branch = st.selectbox("Select Branch", branches)

# Filter data
if selected_branch == "All Branches":
    filtered_df = df.copy()
else:
    filtered_df = df[df["branch"] == selected_branch]

# Total revenue
total_revenue = filtered_df["total_sar"].sum()

st.metric("Total Revenue (SAR)", f"{total_revenue:,.2f}")

# Revenue by product
product_revenue = (
    filtered_df.groupby("product")["total_sar"]
    .sum()
    .sort_values(ascending=False)
)

st.subheader("Revenue by Product")
st.bar_chart(product_revenue)

# Monthly revenue
st.subheader("Monthly Revenue")
monthly_revenue = (
    filtered_df.groupby(filtered_df["date"].dt.to_period("M"))["total_sar"]
    .sum()
)
monthly_revenue.index = monthly_revenue.index.astype(str)

st.line_chart(monthly_revenue)

st.caption("Data source: cafe_sales.csv")

