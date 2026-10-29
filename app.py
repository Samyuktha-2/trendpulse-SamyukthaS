import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="TrendPulse", layout="wide")

BASE_DIR = Path(__file__).parent
DATA_PATH = BASE_DIR / "Data" / "analysed" / "trends_analysed.csv"

data = pd.read_csv(DATA_PATH)

st.title("TrendPulse")
st.caption("Hacker News Trend Analytics")

col1, col2, col3 = st.columns(3)
col1.metric("Total Stories", len(data))
col2.metric("Average Score", round(data["score"].mean(), 2))
col3.metric("Total Comments", int(data["num_comments"].sum()))