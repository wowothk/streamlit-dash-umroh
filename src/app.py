# pylint: disable=missing-module-docstring, missing-function-docstring
import streamlit as st
from components.home import home
from components.trend import trend
from components.market import market

# Set Streamlit to wide mode
st.set_page_config(layout="wide")

def main():
    st.sidebar.title("Dashboard Umroh")
    st.sidebar.write("Made with ❤️ by [Hamba Allah]")

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
