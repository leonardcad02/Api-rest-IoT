#!/usr/bin/env python3
# Importamos paquetes que necesitamos
import os
import requests
import time
import datetime
from threading import Timer



# Consulta los datos del sensor en la IP del Wemos
estacion_metereologica = requests.get('http://192.168.1.72:80')
bus = requests.get('http://192.168.1.74:80')
persona = requests.get('http://192.168.1.76:80')

# Setup del timestamp 
t = time.time()
timegood = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')

# Convierte la respuesta del servidor de Wemos en un diccionario de Python
while (1):
    sensor_data_estacion = estacion_metereologica.json()
    sensor_data_bus = bus.json()
    sensor_data_persona= persona.json()

    # Lectura de estacion Metereologica
    temperatura = sensor_data_estacion['variables']['temperatura']
    humedad = sensor_data_estacion['variables']['humedadd']
    contaminacion = sensor_data_estacion['variables']['co2']
    uv = sensor_data_estacion['variables']['uv']
    ruido = sensor_data_estacion['variables']['ruido']

    # Lectura de bus

    latitud = sensor_data_bus['variables']['latitud']
    longitud = sensor_data_bus['variables']['longitd']
    altitud = sensor_data_bus ['variables']['altitud']
    velocidad = sensor_data_bus['variables']['velocidad']
    
    #lectura de pesonas

    persona = sensor_data_persona['variables']['persona']

    
    print('Estacion Metereologica')
    print (temperatura, humedad, contaminacion, uv,ruido)
    print('/n')
    print ('Bus')
    print (latitud+' '+longitud+' ',+' '+altitud+' '+velocidad)
    print('/n')
    print ('persona')
    print (persona)
    
    
    
    