#!/usr/bin/env python3
# Importamos paquetes que necesitamos
import os
import requests
import time
import datetime



# Consulta los datos del sensor en la IP del Wemos
response = requests.get('http://192.168.1.80:80')
#response2 = requests.get('http://192.168.0.27:80')

# Setup del timestamp 
t = time.time()
timegood = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')

# Convierte la respuesta del servidor de Wemos en un diccionario de Python
sensor_data = response.json()

temperature = sensor_data['variables']['temperature']
humidity = sensor_data['variables']['humidity']
pollution = sensor_data['variables']['contaminacion']



# Hace el promedio de las mediciones
#avtemp = ((temperature+temperature2/2)) 
#avhumi = ((humidity+humidity2)/2)
#avpoll = ((pollution+pollution2)/2)

# Envia el tweet en mi cuenta
print('Soy un bot creado por Cristian \n La temperatura es: {0} ℃ \n La humedad es: {1} %% RH \n La concentración es: {2} %% PPM \n {3}' .format(temperature, humidity, pollution, timegood))