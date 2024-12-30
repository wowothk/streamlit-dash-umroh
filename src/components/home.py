# pylint: disable=missing-module-docstring, missing-function-docstring
import streamlit as st
import pandas as pd
import plotly.express as px
from utils.load_data import load_data, load_geojson
from streamlit_echarts import st_echarts

def home():
    # Load data
    df = load_data()

    # Filter data for the years 2023 and 2022
    data_2023 = df[df['tahun'] == 2023]
    data_2022 = df[df['tahun'] == 2022]

    # Prepare data for ECharts
    options_peserta_umroh = {
        "title": {"text": "Umroh Data by Province"},
        "tooltip": {"trigger": "axis"},
        "legend": {"data": ["2023", "2022"]},
        "xAxis": {
            "type": "category",
            "data": data_2023['provinsi'].tolist()
        },
        "yAxis": {"type": "value"},
        "series": [
            {
                "name": "2023",
                "type": "line",
                "data": data_2023['jumlah'].tolist(),
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
                "name": "2022",
                "type": "line",
                "data": data_2022['jumlah'].tolist(),
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
    st_echarts(options=options_peserta_umroh)

    option_jumlah_ppih = {
        "title": {"text": "Total PPIH by Province"},
        "tooltip": {"trigger": "axis"},
        "legend": {"data": ["A", "B", "C"]},
        "xAxis": {
            "type": "category",
            "data": data_2023['provinsi'].tolist()
        },
        "yAxis": {"type": "value"},
        "series": [
            {
                "name": "A",
                "type": "bar",
                "stack": "total",
                "data": [None if pd.isna(x) else x for x in data_2023['A'].tolist()]
            },
            {
                "name": "B",
                "type": "bar",
                "stack": "total",
                "data": [None if pd.isna(x) else x for x in data_2023['B'].tolist()]
            },
            {
                "name": "C",
                "type": "bar",
                "stack": "total",
                "data": [None if pd.isna(x) else x for x in data_2023['C'].tolist()]
            }
        ]
    }
    # print(option_jumlah_ppih)
    st_echarts(options=option_jumlah_ppih)

    # convertion rate
    option_conversion_rate = {
        "title": {"text": "Conversion Rate by Province"},
        "tooltip": {"trigger": "axis"},
        "legend": {"data": ["2023", "2022"]},
        "xAxis": {
            "type": "category",
            "data": data_2023['provinsi'].tolist()
        },
        "yAxis": {"type": "value"},
        "series": [
            {
                "name": "2023",
                "type": "line",
                "data": [None if pd.isna(x) else x for x in data_2023['convertion_rate'].tolist()]
            },
            {
                "name": "2022",
                "type": "line",
                "data": [None if pd.isna(x) else x for x in data_2022['convertion_rate'].tolist()]
            }
        ]
    }

    gdf = load_geojson()
    gdf = gdf.merge(data_2023, left_on='state', right_on='provinsi', how='right')

    geojson_data = gdf.__geo_interface__

    fig = px.choropleth(
        gdf,
        geojson=geojson_data,
        locations="state",
        featureidkey="properties.state",
        color='convertion_rate',
        color_continuous_scale="Viridis",
        projection="mercator",
        width=800,  # Set the width of the plot
        height=600  # Set the height of the plot
    )
    fig.update_geos(fitbounds="locations", visible=False)

    st.header("Conversion Rate by Province")
    # Display the choropleth map
    st.plotly_chart(fig)

    st_echarts(options=option_conversion_rate)
