# pylint: disable=missing-module-docstring, missing-function-docstring, line-too-long
import streamlit as st
from components.home import home
from components.trend import trend
from components.market import market

# Set Streamlit to wide mode
st.set_page_config(layout="wide", page_title="Dashboard Umroh", page_icon=":kaaba:")

def main():
    st.sidebar.title("Dashboard Umroh")
    st.sidebar.write(
        "This dashboard is created to visualize the condition, trend, and market of Umroh in Indonesia."
    )

     # Navigation
    page = st.sidebar.radio("Please select this", ["Condition", "Trend", "Market"])

    if page == "Condition":
        home()
    elif page == "Trend":
        trend()
    elif page == "Market":
        market()

if __name__ == "__main__":
    main()
