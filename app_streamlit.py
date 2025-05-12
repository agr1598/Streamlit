# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 13:54:41 2025

@author: agonzalez
"""

import streamlit as st
import pandas as pd

# Simulación del DataFrame con los datos proporcionados
data = {
    "QName": [
        "PropertyPlantAndEquipment",
        "PropertyPlantAndEquipment",
        "IntangibleAssetsOtherThanGoodwill",
        "IntangibleAssetsOtherThanGoodwill",
        "RightofuseAssets",
        "RightofuseAssets",
        "InvestmentsInAssociatesAccountedForUsingEquityMethod"
    ],
    "Value": [
        9539000.0,
        23854000.0,
        46980000.0,
        48749000.0,
        51310000.0,
        40486000.0,
        1529000.0
    ],
    "EndDatetime": [
        "2023-01-01", "2022-01-01", "2023-01-01",
        "2022-01-01", "2023-01-01", "2022-01-01", "2023-01-01"
    ],
    "Measure": ["EUR"] * 7,
    "LEI": ["213800JEZBUPZKWJGF49"] * 7,
    "Period": ["2022-12-31"] * 7,
    "IssuerName": ["TECNICAS REUNIDAS, S.A."] * 7,
    "Anchor": ["ifrs-full"] * 7,
    "Anchor_binary": [0] * 7,
    "NACE Classification": [
        "71 Architectural and engineering activities; technical testing and analysi"
    ] * 7,
    "MacroSector": [None] * 7,
    "NCACountry": ["ES"] * 7,
    "HomeMS": ["ES"] * 7
}
df = pd.DataFrame(data)

# Título de la app
st.title("Búsqueda por QName")

# Campo de búsqueda
search_input = st.text_input("Ingrese el QName a buscar:")

# Si se ingresa algún texto, se filtran los datos
if search_input:
    # Se filtra el DataFrame usando una búsqueda que no distingue mayúsculas/minúsculas
    filtered_df = df[df["QName"].str.contains(search_input, case=False, na=False)]
    st.write("Resultados de la búsqueda:")
    st.dataframe(filtered_df)
else:
    st.write("Ingrese un valor en el campo de búsqueda para ver resultados.")
