#!/usr/bin/env python3
# Importamos paquetes que necesitamos
import os
import requests
import time
import datetime
from threading import Timer



# Consulta los datos del sensor en la IP del Wemos
response = requests.get('http://192.168.1.80:80')
#response2 = requests.get('http://192.168.0.27:80')

# Setup del timestamp 
t = time.time()
timegood = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')

# Convierte la respuesta del servidor de Wemos en un diccionario de Python
while (1):
    sensor_data = response.json()

    temperature = sensor_data['variables']['temperature']
    humidity = sensor_data['variables']['humidity']
    pollution = sensor_data['variables']['contaminacion']



    # Hace el promedio de las mediciones
    #avtemp = ((temperature+temperature2/2)) 
    #avhumi = ((humidity+humidity2)/2)
    #avpoll = ((pollution+pollution2)/2)

    # Envia el tweet en mi cuenta

    print (temperature, humidity, pollution)
    Timer(30.0).start()
    