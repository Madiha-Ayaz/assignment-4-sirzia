import streamlit as st

st.set_page_config(page_title="BMI Calculator", layout="centered")

st.title("💪 BMI Calculator")

# Input from user
height = st.number_input("Enter your height (in meters)", min_value=0.1, step=0.01)
weight = st.number_input("Enter your weight (in kilograms)", min_value=1.0, step=0.1)

# Calculate BMI
if height > 0 and weight > 0:
    bmi = weight / (height ** 2)
    st.write(f"### Your BMI is: **{bmi:.2f}**")

    # BMI Category
    if bmi < 18.5:
        st.warning("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.success("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.info("You are overweight.")
    else:
        st.error("You are obese.")
else:
    st.write("👈 Please enter valid height and weight to calculate your BMI.")
