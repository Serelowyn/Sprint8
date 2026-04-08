# --------------- Importaciones

"""Se iran añadiendo conforme a se necesite en el futuro"""
import pandas as pd

# --------------- Fin de las importaciones

"""aqui se traen los dos primeros archivos excel para hacer data frame para analizarlos."""

df_companies = pd.read_csv(r"C:\\Users\\sasor\\Desktop\\Tripleten\\Sprint 8\\proyecto\\moved_project_sql_result_01.csv")

df_locations = pd.read_csv(r"C:\\Users\\sasor\\Desktop\\Tripleten\\Sprint 8\\proyecto\\moved_project_sql_result_04.csv")

"""esto nos permite revisar que se haya cargado correctamente"""
print(df_companies.head())
print(df_locations.head())
