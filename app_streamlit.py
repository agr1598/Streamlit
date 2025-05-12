# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 13:54:41 2025

@author: agonzalez
"""

import streamlit as st
import pandas as pd

# Simulación del DataFrame con los datos proporcionados
df = pd.read_parquet("df.parquet")

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
