# pip install yfinance
# pip install bs4
# pip install nbformat

import yfinance as yf
Tesla=yf.Ticker('TSLA')
tesla_data=Tesla.history(period = 'max')
tesla_data.reset_index(inplace=True) 

#Pregunta 1: Utilice yfinance para extraer datos bursátiles
print(tesla_data.head())

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = r"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"

response = requests.request("GET", url)

soup = BeautifulSoup(response.text,'html.parser')
tables= soup.find_all('table')

# Paso 2: Identificar la tabla relevante que contiene el texto "Tesla Quarterly Revenue"
tesla_revenue_table = None

for table in tables:
    if "Tesla Quarterly Revenue" in table.text:
        tesla_revenue_table = table
        break

# Verificar si se encontró la tabla
if tesla_revenue_table is None:
    print("No se encontró la tabla con el texto 'Tesla Quarterly Revenue'.")
else:
    # Paso 3: Inicializar un DataFrame vacío con columnas "Date" y "Revenue"
    tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])
    
    # Paso 4: Recorrer las filas de la tabla relevante
    rows = []
    for row in tesla_revenue_table.find_all('tr')[1:]:  # Saltar el encabezado de la tabla
        cols = row.find_all('td')
        
        if len(cols) >= 2:  # Asegurarse de que la fila tiene al menos dos columnas
            date = cols[0].text.strip()  # Columna de fecha
            revenue = cols[1].text.strip()  # Columna de ingresos
            
            # Paso 5: Limpiar los datos de ingresos (quitar signos de dólar y comas)
            revenue = revenue.replace('$', '').replace(',', '')
            
            # Agregar la fila a la lista de filas
            rows.append({"Date": date, "Revenue": revenue})
    
    # Paso 6: Agregar las filas al DataFrame usando pd.concat()
    tesla_revenue = pd.concat([tesla_revenue, pd.DataFrame(rows)], ignore_index=True)

    # Mostrar el DataFrame resultante
    print(tesla_revenue.tail())


import yfinance as yf
Amd=yf.Ticker('AMD')
gme_data=Amd.history(period = 'max')
gme_data.reset_index(inplace=True) 

#Pregunta 3: Utilice yfinance para extraer datos bursátiles
print(gme_data.head())


import yfinance as yf
import matplotlib.pyplot as plt

# Definir la función make_graph para graficar los datos de Tesla
def make_graph(data, title):
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Close'], label="Precio de Cierre")
    plt.title(title)
    plt.xlabel("Fecha")
    plt.ylabel("Precio de Cierre (USD)")
    plt.legend()
    plt.grid(True)
    plt.show()

# Descargar los datos históricos de Tesla (TSLA) con el período máximo
tesla = yf.Ticker("TSLA")
tesla_history = tesla.history(period="max")

# Llamar a la función make_graph para graficar los datos de Tesla
make_graph(tesla_history, "Gráfico del Precio de Cierre de las Acciones de Tesla")




# Definir la función make_graph para graficar los datos de Tesla
def make_graph(data, title):
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Close'], label="Precio de Cierre")
    plt.title(title)
    plt.xlabel("Fecha")
    plt.ylabel("Precio de Cierre (USD)")
    plt.legend()
    plt.grid(True)
    plt.show()

# Descargar los datos históricos de Tesla (TSLA) con el período máximo
amd = yf.Ticker("AMD")
amd_history = amd.history(period="max")

# Llamar a la función make_graph para graficar los datos de Tesla
make_graph(amd_history, "Gráfico del Precio de Cierre de las Acciones de AMD")