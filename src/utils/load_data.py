# pylint: disable=missing-module-docstring, missing-function-docstring, line-too-long
import os
import pandas as pd
import geopandas as gpd

def load_data():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, '../data/compiled_umroh.csv')
    return pd.read_csv(file_path)

def load_geojson():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, '../data/indonesia.geojson')
    gdf = gpd.read_file(file_path)
    gdf["state"] = gdf["state"].str.lower()
    gdf["state"] = gdf["state"].str.replace("yogyakarta", "daerah istimewa yogyakarta")
    gdf["state"] = gdf["state"].str.replace("jakarta raya", "dki jakarta")
    gdf["state"] = gdf["state"].str.replace("bangka-belitung", "kepulauan bangka belitung")
    return gdf

def load_data_trend():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, '../data/multiTimeline.csv')
    return pd.read_csv(file_path)

def load_data_trend_by_province():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, '../data/trend_by_province.csv')
    return pd.read_csv(file_path)
