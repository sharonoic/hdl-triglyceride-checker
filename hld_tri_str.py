import streamlit as st

st.title("HDL/Triglyceride Ratio Checker")

st.markdown("This tool helps you calculate your TG/HDL ratio, a cardiovascular and metabolic health marker. "
            "Values are converted automatically. Lower ratios are generally better.")

hdl_unit = st.radio("Is your HDL in mmol/L?", ("Yes", "No"))
if hdl_unit == "Yes":
    hdl = st.number_input("Enter your HDL (mmol/L):", min_value=0.0, step=0.1)
    hdl_mg = hdl * 38.67
else:
    hdl_mg = st.number_input("Enter your HDL (mg/dL):", min_value=0.0, step=1.0)

tri_unit = st.radio("Is your Triglycerides in mmol/L?", ("Yes", "No"))
if tri_unit == "Yes":
    tri = st.number_input("Enter your Triglycerides (mmol/L):", min_value=0.0, step=0.1)
    tri_mg = tri * 88.57
else:
    tri_mg = st.number_input("Enter your Triglycerides (mg/dL):", min_value=0.0, step=1.0)

if hdl_mg > 0 and tri_mg > 0:
    ratio = tri_mg / hdl_mg
    st.markdown(f"### TG/HDL Ratio: **{ratio:.2f}**")
    if ratio > 2:
        st.error("Your ratio is **not ideal**. This may suggest increased cardiovascular/metabolic risk.")
    elif ratio > 1.5:
        st.warning("Your ratio is **acceptable**, but not ideal.")
    else:
        st.success("Congrats! Your TG/HDL ratio is **ideal**.")
