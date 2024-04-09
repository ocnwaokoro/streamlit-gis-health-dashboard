import streamlit as st
import leafmap.kepler as leafmap
from keplergl import KeplerGl
import leafmap.kepler as leafmap
import geopandas as gpd
import pandas as pd
import numpy as np

def app():
  APP_TITLE = "Ghana Health Access & Population Report"
  APP_SUB_TITLE = "Source: Ghana Statistical Service & Clinton Health Access Initiative"

  config = {'version': 'v1',
  'config': {'visState': {'filters': [],
    'layers': [{'id': 'grnz7jp',
      'type': 'geojson',
      'config': {'dataId': 'Facilities',
        'label': 'Facilities',
        'color': [55, 179, 139],
        'highlightColor': [252, 242, 26, 255],
        'columns': {'geojson': '_geojson'},
        'isVisible': True,
        'visConfig': {'opacity': 0.8,
        'strokeOpacity': 0.8,
        'thickness': 0.5,
        'strokeColor': [11, 95, 101],
        'colorRange': {'name': 'Custom Palette',
          'type': 'custom',
          'category': 'Custom',
          'colors': ['#12939A',
          '#DDB27C',
          '#88572C',
          '#FF991F',
          '#F15C17',
          '#223F9A',
          '#DA70BF',
          '#125C77',
          '#4DC19C',
          '#776E57',
          '#17B8BE',
          '#F6D18A',
          '#B7885E',
          '#FFCB99',
          '#F89570',
          '#829AE3',
          '#E79FD5',
          '#1E96BE',
          '#89DAC1',
          '#B3AD9E']},
        'strokeColorRange': {'name': 'Global Warming',
          'type': 'sequential',
          'category': 'Uber',
          'colors': ['#5A1846',
          '#900C3F',
          '#C70039',
          '#E3611C',
          '#F1920E',
          '#FFC300']},
        'radius': 10,
        'sizeRange': [0, 10],
        'radiusRange': [0, 50],
        'heightRange': [0, 500],
        'elevationScale': 5,
        'enableElevationZoomFactor': True,
        'stroked': True,
        'filled': True,
        'enable3d': False,
        'wireframe': False},
        'hidden': False,
        'textLabel': [{'field': None,
          'color': [255, 255, 255],
          'size': 18,
          'offset': [0, 0],
          'anchor': 'start',
          'alignment': 'center'}]},
      'visualChannels': {'colorField': None,
        'colorScale': 'quantile',
        'strokeColorField': None,
        'strokeColorScale': 'quantile',
        'sizeField': None,
        'sizeScale': 'linear',
        'heightField': None,
        'heightScale': 'linear',
        'radiusField': None,
        'radiusScale': 'linear'}},
      {'id': 'v4ysqjj',
      'type': 'geojson',
      'config': {'dataId': 'Regions',
        'label': 'Regions',
        'color': [221, 178, 124],
        'highlightColor': [252, 242, 26, 255],
        'columns': {'geojson': '_geojson'},
        'isVisible': True,
        'visConfig': {'opacity': 0.8,
        'strokeOpacity': 0.8,
        'thickness': 1,
        'strokeColor': [25, 20, 16],
        'colorRange': {'name': 'ColorBrewer Greens-9',
          'type': 'singlehue',
          'category': 'ColorBrewer',
          'colors': ['#f7fcf5',
          '#e5f5e0',
          '#c7e9c0',
          '#a1d99b',
          '#74c476',
          '#41ab5d',
          '#238b45',
          '#006d2c',
          '#00441b']},
        'strokeColorRange': {'name': 'Global Warming',
          'type': 'sequential',
          'category': 'Uber',
          'colors': ['#5A1846',
          '#900C3F',
          '#C70039',
          '#E3611C',
          '#F1920E',
          '#FFC300']},
        'radius': 10,
        'sizeRange': [0, 10],
        'radiusRange': [0, 50],
        'heightRange': [0, 500],
        'elevationScale': 100,
        'enableElevationZoomFactor': True,
        'stroked': True,
        'filled': True,
        'enable3d': False,
        'wireframe': False},
        'hidden': False,
        'textLabel': [{'field': None,
          'color': [255, 255, 255],
          'size': 18,
          'offset': [0, 0],
          'anchor': 'start',
          'alignment': 'center'}]},
      'visualChannels': {'colorField': {'name': 'POPULATION', 'type': 'real'},
        'colorScale': 'quantize',
        'strokeColorField': None,
        'strokeColorScale': 'quantile',
        'sizeField': None,
        'sizeScale': 'linear',
        'heightField': {'name': 'POPULATION', 'type': 'real'},
        'heightScale': 'linear',
        'radiusField': None,
        'radiusScale': 'linear'}}],
    'interactionConfig': {'tooltip': {'fieldsToShow': {'Facilities': [{'name': 'FACILITY',
          'format': None},
        {'name': 'REGION', 'format': None},
        {'name': 'DISTRICT', 'format': None},
        {'name': 'TYPE', 'format': None},
        {'name': 'OWNERSHIP', 'format': None}],
        'Regions': [{'name': 'REGION', 'format': None},
        {'name': 'POPULATION', 'format': None},
        {'name': 'FACILITIES', 'format': None}]},
      'compareMode': False,
      'compareType': 'absolute',
      'enabled': True},
      'brush': {'size': 0.5, 'enabled': False},
      'geocoder': {'enabled': False},
      'coordinate': {'enabled': False}},
    'layerBlending': 'normal',
    'splitMaps': [],
    'animationConfig': {'currentTime': None, 'speed': 1}},
    'mapState': {'bearing': 0,
    'dragRotate': False,
    'latitude': 7.961231438337197,
    'longitude': -1.3025861578682738,
    'pitch': 0,
    'zoom': 5.9790399657124,
    'isSplit': False},
    'mapStyle': {'styleType': 'light',
    'topLayerGroups': {},
    'visibleLayerGroups': {'label': True,
      'road': True,
      'border': False,
      'building': False,
      'water': True,
      'land': True,
      '3d building': True},
    'threeDBuildingColor': [218.82023004728686,
      223.47597962276103,
      223.47597962276103],
    'mapStyles': {}},
    'uiState': {'readOnly': True}}}

  width = 600
  height = 600

  @st.cache_resource(show_spinner="Loading Map...")
  def REGION_MAP():
      m = leafmap.Map(center=(7.9465, -1.0232), width=width,height=height) 
      regions = gpd.read_file("data/GH-2/gh-regions-polygons.geojson")
      df_fac_reg = pd.read_csv("data/GH/gh-facilities-per-region.csv")
      df_pop_reg = pd.read_csv("data/GH/gh-population-count-per-region.csv")
      df_fac_pop_reg = pd.DataFrame()
      df_fac_pop_reg["region"] = df_fac_reg["Region_202"].unique()
      df_fac_pop_reg = df_fac_pop_reg.dropna()
      for region in df_fac_pop_reg["region"]:
          pop = df_pop_reg[df_pop_reg["Region_202"]==region]["VALUE"].sum()
          df_fac_pop_reg.loc[list(df_fac_pop_reg["region"]).index(region),"POPULATION"] = pop
          fac = len(df_fac_reg[df_fac_reg["Region_202"]==region])
          df_fac_pop_reg.loc[list(df_fac_pop_reg["region"]).index(region),"FACILITIES"] = fac
      df_fac_pop_reg['region'] = df_fac_pop_reg['region'].map(str.upper)
      regions_pop_fac_df = regions.join(df_fac_pop_reg.set_index('region'), on="REGION")
      reg = regions_pop_fac_df[['REGION','POPULATION','FACILITIES','geometry']]
      m.add_gdf(reg, layer_name='Regions')
      m.config = config
      return m
  st.title(APP_TITLE)
  st.caption(APP_SUB_TITLE)
  col1, col2 = st.columns(2)
  with col1:
      st.markdown("<h2 style='text-align: center; color: black;'>Regions Map </h2>", unsafe_allow_html=True)
      REGION_MAP().to_streamlit(width=width, height=height)
  with col2:
      st.markdown("<h2 style='text-align: center; color: black;'>Regions Info </h2>", unsafe_allow_html=True)
