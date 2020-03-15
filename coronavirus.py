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

    def get_data(self):
        try:
            print("site")
            self.driver.get('https://www.worldometers.info/coronavirus/')
            #self.driver.get('C:\\Users\\ruffineo\\Downloads\\HTML_EXAMPLE\\Coronavirushtml.html')
            print("driver get OK")
            try:
                tbl = self.driver.find_element_by_id('main_table_countries')#.get_attribute('outerHTML')
                #print("table from site OK", tbl)
                #xml = html.fromstring(tbl)
                #tabla =  tbl.xpath("//table[@id='main_table_countries']")[0]
                for row in tbl.find_elements_by_css_selector('tr'):
                    for cell in row.find_elements_by_tag_name('td'):
                        if cell.text == 'Paraguay':
                            print(cell.text)
                #cntry = tbl.find_element_by_xpath("//td[contains(text(), 'Paraguay ')]")#.get_attribute('outerHTML')
                #country_element = tbl.find_element_by_xpath("//td[contains(text(), 'Paraguay ')]")
                #print('country:', cntry)
                #fila = cntry.find_element_by_xpath("./..").get_attribute()
                #print('fila:', fila)
                #print('fila:', fila)
                #df  = pd.read_html(cntry)
                #df = pd.DataFrame(df, columns = ['Index','Pais','Total','Nuevos','TotalMuertos','NuevosMuertos','Recuperados','Activos','Criticos','PorcentajePor1MHabitantes'])
                #print('df: ', str(df[0]))
                #cadena = str(df[0])
                #print('PY:', cadena.splitlines())
                #print(df)
                #print(df.str.contains('|'.join('Paraguay')).any(level=0))
                #all_columns_list = df.tolist() #get a list of all the column names
                #for col in all_columns_list: print(col)
                #print(type(cadena_full))
                #print(cadena_full)
                #for line in df:
                #    if line.str.contains('|'.join('Paraguay')).any(level=0):
                    #print(type(line))
            except Exception as error:
                print("{}".format(error))
            try:
                table = self.driver.find_element_by_id('main_table_countries')#find_element_by_xpath('//*[@id="main_table_countries"]/tbody[1]')
                print("table from site OK")
                country_element = table.find_element_by_xpath("//td[contains(text(), 'Paraguay ')]")
                print("Country stats OK", country_element.text)
                row = country_element.find_element_by_xpath("./..")
                print("Row with info OK:", row.text)
                data = row.text.split(" ")
                print("data split, total " + data[1] + " new " + data[2] + " active " + data[3] + " seriedad " + data[4] + " porcentaje " + data[5])# + " recovered " + data[6] + " critical " + data[7])
                total_cases = data[1]
                new_cases = data[2]
                #total_deaths = data[3]
                #new_deaths = data[4]
                active_cases = data[3]
                #total_recovered = data[6]
                serious_critical = data[4]
                porcentaje = data[5]
            except Exception as e:
                print("{}".format(e))

            #total_cases = row.find_element_by_class_name('sorting_1')
            #new_cases = row.find_element_by_xpath("//td[3]")
            #total_deaths = row.find_element_by_xpath("//td[4]")
            #new_deaths = row.find_element_by_xpath("//td[5]")
            #active_cases = row.find_element_by_xpath("//td[6]")
            #total_recovered = row.find_element_by_xpath("//td[7]")
            #serious_critical = row.find_element_by_xpath("//td[8]")
            print("Country: " + country_element.text)
            print("Total cases: " + total_cases)
            print("New cases: " + new_cases)
            #print("Total deaths: " + total_deaths)
            #print("New deaths: " + new_deaths)
            print("Active cases: " + active_cases)
            #print("Total recovered: " + total_recovered)
            print("Serious, critical cases: " + serious_critical)
            print("Porcentaje: " + porcentaje)

            send_mail(country_element.text, 
                      total_cases, 
                      new_cases, 
                      #total_deaths, 
                      #new_deaths, 
                      active_cases, 
                      #total_recovered, 
                      serious_critical,
                      porcentaje)



            self.driver.close()
        except:
            self.driver.quit()

def send_mail(country_element, 
              total_cases, 
              new_cases, 
              #total_deaths, 
              #new_deaths, 
              active_cases, 
              #total_recovered, 
              serious_critical,
              porcentaje):
    print("mail")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    print("server OK")
    server.ehlo()
    print("server ehlo OK")
    server.starttls()
    print("server startTLS OK")
    server.ehlo()
    print("server ehloTLS OK")
    try:
        server.login('coronavirusmailer@gmail.com', 'Papito01')
        print("server login OK")
    except Exception as e:
        print("{}".format(e))

    subject = 'Estadisticas del Coronavirus en el pais!'

    ##\nTotal deaths: ' + total_deaths + '\
    #    \nNew deaths: ' + new_deaths + '\
    #    \nTotal recovered: ' + total_recovered + '\
        
    body = 'CoronaVirus en ' + country_element + '\
        \nDatos a la fecha en cuanto a infectados:\
        \nTotal de casos: ' + total_cases +'\
        \nNuevos casos: ' + new_cases + '\
        \nPacientes activos: ' + active_cases + '\
        \nCasos criticos: ' + serious_critical  + '\
        \nPorcentaje infectados en la poblacion: ' + porcentaje  + '%' + '\
        \nMas informacion: https://www.worldometers.info/coronavirus/'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'coronavirusmailer@mail.com',
        ['familiaruffinellivera@gmail.com','veroruffi92@gmail.com','ruffineo@personal.com.py'],
        msg
    )
    print('Hey Email has been sent!')

    server.quit()

bot = Coronavirus()
bot.get_data()