from selenium import webdriver
from time import sleep
import re
from datetime import datetime
import smtplib
import re
import pandas as pd
from lxml import html

class Coronavirus():
    def __init__(self):
        print("webdriver")
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome()

    def get_data(self):
        try:
            print("site")
            self.driver.get('https://www.worldometers.info/coronavirus/')
            #self.driver.get('C:\\Users\\ruffineo\\Downloads\\HTML_EXAMPLE\\Coronavirushtml.html')
            print("driver get OK")
            try:
                tbl = self.driver.find_element_by_id('main_table_countries_today')#.get_attribute('outerHTML')
                print("encontro tabla")
                paises = []
                for row in tbl.find_elements_by_css_selector('tr'):
                    detalles = []
                    for cell in row.find_elements_by_tag_name('td'):
                        if cell.text != '':
                            detalles.append(cell.text)
                        else:
                            detalles.append('0')
                    if detalles!=[]:
                        paises.append(detalles)    
            except Exception as error:
                paises = []
                print("{}".format(error))
            try:
                print("table from site OK")
                paraguay = []
                for index, item in enumerate(paises):
                    if item[0]=='Paraguay':
                        paraguay = paises[index]
                        pais = paraguay[0]
                        total = paraguay[1]
                        nuevos = paraguay[2]
                        totalmuertos = paraguay[3]
                        nuevosmuertos = paraguay[4]
                        recuperados = paraguay[5]
                        activos = paraguay[6]
                        criticos = paraguay[7]
                        porcentaje = paraguay[8]
            except Exception as e:
                print("{}".format(e))
            if pais != '':
                send_mail(pais,total,nuevos,totalmuertos,nuevosmuertos,activos,recuperados,criticos,porcentaje)
            else:
                print('No se encontraron datos.')
            self.driver.close()
        except:
            self.driver.quit()

def send_mail(country_element, 
              total_cases, 
              new_cases, 
              total_deaths, 
              new_deaths, 
              active_cases, 
              total_recovered, 
              serious_critical,
              porcentaje):
    print("mail")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    try:
        server.login('coronavirusmailer@gmail.com', 'Papito01')
        print("server login OK")
    except Exception as e:
        print("{}".format(e))

    subject = 'Estadisticas del Coronavirus en el pais!'
    body = 'CoronaVirus en ' + country_element + '\
        \nDatos a la fecha en cuanto a infectados:\
        \nTotal de casos: ' + total_cases +'\
        \nNuevos casos: ' + new_cases + '\
        \nTotal muertos: ' + total_deaths + '\
        \nMuertes nuevas: ' + new_deaths + '\
        \nPacientes activos: ' + active_cases + '\
        \nTotal recuperados: ' + total_recovered + '\
        \nCasos criticos: ' + serious_critical  + '\
        \n% Sobre 1M habitantes: ' + porcentaje  + '%' + '\
        \nMas informacion: https://www.worldometers.info/coronavirus/'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'coronavirusmailer@mail.com',
        ['MAIL RECIPIENTS GOES HERE'],
        msg
    )
    print('Hey Email has been sent!')

    server.quit()

bot = Coronavirus()
bot.get_data()