# --------------- Importaciones

"""Se iran añadiendo conforme a se necesite en el futuro"""
import pandas as pd

# --------------- Fin de las importaciones

"""aqui se traen los dos primeros archivos excel para hacer data frame para analizarlos."""

df_companies = pd.read_csv("/datasets/project_sql_result_01.csv")
df_locations = pd.read_csv("/datasets/project_sql_result_04.csv")
