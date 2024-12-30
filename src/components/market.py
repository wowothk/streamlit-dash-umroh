# pylint: disable=missing-module-docstring, missing-function-docstring, line-too-long
import streamlit as st
from streamlit_echarts import st_echarts
from utils.load_data import load_data

def market():
    # Load data
    df = load_data()

    # Prepare data for ECharts
    # Sort data by 'islam' column in descending order
    data_2023 = df[df['tahun'] == 2023]
    data_2022 = df[df['tahun'] == 2022]

    sorted_df = data_2023.sort_values(by='islam', ascending=True)

    options_penduduk_muslim = {
        "title": {"text": "Pendudukan Muslim by Province"},
        "tooltip": {"trigger": "axis"},
        "xAxis": {
            "type": "value"
        },
        "yAxis": {
            "type": "category",
            "data": sorted_df['provinsi'].tolist(),
            "axisLabel": {
                "interval": 0,
            }
        },
        "series": [
            {
                "name": "travel umroh",
                "type": "bar",
                "data": sorted_df['islam'].tolist()
            },
        ],
        "dataZoom": [
            {
                "type": "slider",
                "yAxisIndex": 0,
                "filterMode": "empty",
                "start": 80,
                "end": 100
            }
        ],
        "grid": {
            "left": "10%"
        }
    }

    # Render ECharts
    st_echarts(options=options_penduduk_muslim)

    options_peserta_umroh = {
        "title": {"text": "Persentase Peserta Umroh"},
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
                "data": data_2023['aquisition_rate'].tolist(),
            },
            {
                "name": "2022",
                "type": "line",
                "data": data_2022['aquisition_rate'].tolist()
            }
        ]
    }

    # Render ECharts
    st_echarts(options=options_peserta_umroh)
