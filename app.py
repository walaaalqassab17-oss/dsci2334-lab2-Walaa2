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
