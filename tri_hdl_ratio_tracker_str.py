if not data.empty and tri_col in data.columns and hdl_col in data.columns:
    if tri_unit == "mmol/L":
        tri_mg = data[tri_col] * 88.57
    else:
        tri_mg = data[tri_col]

    if hdl_unit == "mmol/L":
        hdl_mg = data[hdl_col] * 38.67
    else:
        hdl_mg = data[hdl_col]

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
