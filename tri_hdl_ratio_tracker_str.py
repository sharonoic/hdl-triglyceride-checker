import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Triglyceride/HDL Ratio Tracker")
st.markdown("Track your triglyceride-to-HDL ratio over time and monitor your health status.")

hdl_unit = st.selectbox("HDL unit", ["mg/dL", "mmol/L"])
tri_unit = st.selectbox("Triglycerides unit", ["mg/dL", "mmol/L"])

hdl_col = f"HDL ({hdl_unit})"
tri_col = f"Triglycerides ({tri_unit})"

data = st.data_editor(
    pd.DataFrame({
        "Date": [],
        tri_col: [],
        hdl_col: []
    }),
    num_rows="dynamic",
    use_container_width=True
)

if not data.empty and tri_col in data.columns and hdl_col in data.columns:
    try:
        tri_mg = data[tri_col] * (88.57 if tri_unit == "mmol/L" else 1)
        hdl_mg = data[hdl_col] * (38.67 if hdl_unit == "mmol/L" else 1)

        data["TG/HDL Ratio"] = tri_mg / hdl_mg

        def categorize_ratio(ratio):
            if ratio <= 1.5:
                return "Ideal"
            elif ratio <= 2:
                return "Acceptable"
            else:
                return "High"

        data["Category"] = data["TG/HDL Ratio"].apply(categorize_ratio)

        fig = px.scatter(
            data,
            x="Date",
            y="TG/HDL Ratio",
            color="Category",
            color_discrete_map={
                "Ideal": "green",
                "Acceptable": "orange",
                "High": "red"
            },
            title="TG/HDL Ratio Over Time"
        )
        fig.update_traces(mode="lines+markers")
        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error("Please make sure all values are filled in with valid numbers.")
