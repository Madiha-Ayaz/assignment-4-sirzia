import streamlit as st
import pandas as pd

st.title("Simple Data Dashboard")

# Upload CSV file
uploaded_file = st.file_uploader("CHOOSE A CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Data Review
    st.subheader("Data Review")
    st.write(df.head())

    # Data Summary
    st.subheader("Data Summary")
    st.write(df.describe())

    # Filter Data
    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)

    unique_values = df[selected_column].dropna().unique()
    selected_value = st.selectbox("Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    # Plot Data
    st.subheader("Plot Data")
    numeric_columns = df.select_dtypes(include='number').columns.tolist()

    if not numeric_columns:
        st.warning("No numeric columns available for plotting.")
    else:
        x_column = st.selectbox("Select x-axis column", columns)
        y_column = st.selectbox("Select y-axis column", numeric_columns)

        if st.button("Generate Plot"):
            try:
                # Clean up data
                plot_df = filtered_df[[x_column, y_column]].dropna()

                # Use line_chart with set_index if x_column is not numeric
                if pd.api.types.is_numeric_dtype(plot_df[x_column]):
                    st.line_chart(plot_df.set_index(x_column))
                else:
                    st.line_chart(plot_df.set_index(pd.Index(range(len(plot_df)))))

            except Exception as e:
                st.error(f"Error generating plot: {e}")

else:
    st.write("Waiting for CSV file upload...")
