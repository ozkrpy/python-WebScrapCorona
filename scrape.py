#PAGINA EJEMPLO
#https://medium.com/@ankushchoubey/how-to-download-dataset-from-kaggle-7f700d7f9198

#DESCARGA DATASET
#kaggle datasets download -d sudalairajkumar/novel-corona-virus-2019-dataset 
 
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

# First, look at everything.
from subprocess import check_output
class Scrape():
    def __init__(self):
        print("webdriver")
        data = pd.read_csv('./data/covid_19_data.csv')
        casos = pd.read_csv('./data/time_series_covid_19_confirmed.csv')
        py = data.loc[(data["Country/Region"]=="Paraguay")]
        us = data.loc[(data["Country/Region"]=="Mainland China")]

        graficar(py)

def graficar(pais):
    fechas_x = pd.to_datetime(pais["Last Update"]).dt.strftime('%d/%m')
    print(fechas_x)
    confirmados_y = pais["Confirmed"]
    muertes_y = pais["Deaths"]
    recuperados_y = pais["Recovered"]

    plt.plot(fechas_x,confirmados_y)
    plt.plot(fechas_x,muertes_y)
    plt.plot(fechas_x,recuperados_y)

    plt.show()

bot = Scrape()