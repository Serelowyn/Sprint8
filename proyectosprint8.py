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
plt.title("num de viajes por empresa de taxis")
plt.xlabel("empresa")
plt.ylabel("cantidad de viajes")
plt.tight_layout()
plt.show()

"""top10 barrios por finalizacion de viajes"""
top10_locations = df_locations.sort_values(by="average_trips", ascending=False).head(10)

plt.figure(figsize=(10,6))
plt.bar(top10_locations["dropoff_location_name"], top10_locations["average_trips"], color="orange")
plt.xticks(rotation=45)
plt.title("top10 barrios por finalizacion de viajes")
plt.xlabel("barrio")
plt.ylabel("promedio de viajes")
plt.tight_layout()
plt.show()


# sacar conclusiones basadas en cada gráfico y explicar los resultados

""" En el primer grafico (num de viajes por empresa y taxis), vemos que flash cab lidera en cantidad de viajes superando a cualquier otra por minimo, casi el doble de rendimiento. SIendo solo el top 5 que se le acerca, las demas son demasiado menores las cantidades en viajes. Muy problablemente esto se deba a que tenemos bastantes empresas y es normal ver la distribucion de viajes tan distinta, sin embargo que exista una de tal nivel quiere decir que hay mas contexto que nos hace falta, muy probablemente sea la empresa mas grande en general, que permita mas inversion en activo para seguir con las operaciones con mas frecuencia que la competencia."""

"""en el segundo grafico(top10 barrios por finalizacion de viajes) vemos que Loop y rivernorth estan casi a la par, siendo los mas populares y de ahi el top3 es streetville, siento este el top que opaca a las demas destinaciones, quizas sea el atractivo turistico y ademas el tamaño del lugar, ya que lugares con mas espacio, suele tener distintos puntos para aprovechar la visita de las personas como por ejemplo: recuerdos o souvenirs, comida, atracciones, etc."""