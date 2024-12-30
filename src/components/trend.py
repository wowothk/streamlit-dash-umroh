# pylint: disable=missing-module-docstring, missing-function-docstring, line-too-long
import pandas as pd
from streamlit_echarts import st_echarts
from utils.load_data import load_data_trend, load_data_trend_by_province

def trend():
    # Load data
    df = load_data_trend()

    # Prepare data for ECharts
    options_trends_umroh = {
        "title": {"text": "Trend by Keyword"},
        "tooltip": {"trigger": "axis"},
        "legend": {"data": ["travel umroh", "biaya umroh", "doa umroh"]},
        "xAxis": {
            "type": "category",
            "data": df['Week'].tolist()
        },
        "yAxis": {"type": "value"},
        "series": [
            {
                "name": "travel umroh",
                "type": "line",
                "data": df['travel umroh: (Indonesia)'].tolist(),
                "markPoint": {
                    "data": [
                        {"type": "max", "name": "Max"},
                        {"type": "min", "name": "Min"}
                    ]
                },
                "markLine": {
                    "data": [{"type": "average", "name": "Avg"}]
                }
            },
            {
                "name": "biaya umroh",
                "type": "line",
                "data": df['biaya umroh: (Indonesia)'].tolist(),
                "markPoint": {
                    "data": [
                        {"type": "max", "name": "Max"},
                        {"type": "min", "name": "Min"}
                    ]
                },
                "markLine": {
                    "data": [{"type": "average", "name": "Avg"}]
                }
            },
            {
                "name": "doa umroh",
                "type": "line",
                "data": df['doa umroh: (Indonesia)'].tolist(),
                "markPoint": {
                    "data": [
                        {"type": "max", "name": "Max"},
                        {"type": "min", "name": "Min"}
                    ]
                },
                "markLine": {
                    "data": [{"type": "average", "name": "Avg"}]
                }
            }
        ]
    }

    # Render ECharts
    st_echarts(options=options_trends_umroh)

    trend_by_province = load_data_trend_by_province()

    option_trend_by_province = {
        "title": {"text": "Trend by Province"},
        "tooltip": {"trigger": "axis"},
        "legend": {"data": ["travel umroh", "biaya umroh", "doa umroh"]},
        "xAxis": {
            "type": "category",
            "data": trend_by_province['Region'].tolist()
        },
        "yAxis": {"type": "value"},
        "series": [
            {
                "name": "travel umroh",
                "type": "bar",
                "stack": "total",
                "data": [None if pd.isna(x) else x for x in trend_by_province['travel umroh: (2024)'].tolist()]
            },
            {
                "name": "biaya umroh",
                "type": "bar",
                "stack": "total",
                "data": [None if pd.isna(x) else x for x in trend_by_province["biaya umroh: (2024)"].tolist()]
            },
            {
                "name": "doa umroh",
                "type": "bar",
                "stack": "total",
                "data": [None if pd.isna(x) else x for x in trend_by_province["doa umroh: (2024)"].tolist()]
            }
        ]
    }

    st_echarts(options=option_trend_by_province)
