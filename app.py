import streamlit as st
import pandas as pd
import plotly.express as px

st.title("AI Business Dashboard")

data = {
    "Region": ["East", "West", "North", "South"],
    "Revenue": [1200, 900, 700, 1000]
}

df = pd.DataFrame(data)

query = st.text_input("Ask a business question")

if query:
    st.write("Generated Dashboard")
    fig = px.bar(df, x="Region", y="Revenue")
    st.plotly_chart(fig)
