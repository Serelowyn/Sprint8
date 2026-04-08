# --------------- Importaciones

"""Se iran añadiendo conforme a se necesite en el futuro"""
import pandas as pd
import matplotlib.pyplot as plt

# --------------- Fin de las importaciones

"""aqui se traen los dos primeros archivos excel para hacer data frame para analizarlos."""

df_companies = pd.read_csv(r"C:\\Users\\sasor\\Desktop\\Tripleten\\Sprint 8\\proyecto\\moved_project_sql_result_01.csv")

df_locations = pd.read_csv(r"C:\\Users\\sasor\\Desktop\\Tripleten\\Sprint 8\\proyecto\\moved_project_sql_result_04.csv")

"""esto nos permite revisar que se haya cargado correctamente"""
print(df_companies.head())
print(df_locations.head())

"""aqui se verifica el tipo de datos de cada una"""
print(df_companies.info())
print(df_locations.info())

print(df_companies.dtypes)
print(df_locations.dtypes)
"""con esto se comprueba que los datos de nombres pertencen a string, y los int y float corresponden a su naturaleza en ambos data frames. no se requiere limpieza adicional"""

# identificar los 10 principales barrios en términos de finalización del recorrido

"""se hace una agrupacion por la columna average_trips, poniendo los 10 mas altos que pide la instruccion"""
top10_locations = df_locations.sort_values(by="average_trips", ascending=False).head(10)
print(top10_locations)

# hacer gráficos: empresas de taxis y número de viajes, los 10 barrios principales por número de finalizaciones

"""empresas de taxis y num de viajes"""
plt.figure(figsize=(12,6))
plt.bar(df_companies["company_name"], df_companies["trips_amount"], color="skyblue")
plt.xticks(rotation=90, fontsize=8)
plt.title("numero de viajes por empresa de taxis (15-16 de noviembre del 2017)")
plt.xlabel("empresa")
plt.ylabel("cantidad de viajes")
plt.tight_layout()
plt.show()
