from netCDF4 import Dataset
import numpy as np
import subprocess
import pandas as pd
import sys

day = sys.argv[1]
year = sys.argv[2]


#### MAIN  ####

file_output = subprocess.check_output(f'ls data_{day}_{year} | grep OR', shell = True).decode('utf-8')
file_list = file_output.split('\n')
file_list.remove('')



df = pd.DataFrame({'time':[], 'pressure': [], 'wind_speed': [], 'wind_direction': [], 'lat': [], 'lon': []})

for file in file_list:
    file = f'data_{day}_{year}/{file}'
    ### Obtaining data
    data = Dataset(file)

    wind_speed = data.variables['wind_speed'][:]
    wind_direction = data.variables['wind_direction'][:]
    lat = data.variables['lat'][:]
    lon = data.variables['lon'][:]
    pressure = data.variables['pressure'][:]
    
    #date
    output = subprocess.check_output(f'ncinfo {file} | grep time_coverage_end', shell=True).decode('utf-8')
    date = pd.to_datetime(output.replace('    time_coverage_end: ','').replace('Z\n',''),format='%Y-%m-%dT%H:%M:%S')


    #### Limits

    # Guanacaste límites 9.55 - 11.21,-85.90 - -84.90 --> Provincia entera
    # Costa Rica -86.2 - -82.3 y 7.9 - 11.3
    guana_lat = (7.9<lat)*(lat<11.3)#--> 10.2 - 10.6 Zona plana 
    guana_lon = (-86.2<lon)*(lon<-82.3)#--> -85.6 - -85.15 Zona plana 
    guana_pre = (700<pressure)
    guanacaste = guana_lat*guana_lon*guana_pre

    #Mover a un dataframe pequeño
    
    for i in range(len(wind_speed[guanacaste])):
        if wind_direction[guanacaste][i] != '--':
            df_i = pd.DataFrame({'time':[date],
            'pressure': [pressure[guanacaste][i]],
            'wind_speed': [wind_speed[guanacaste][i]],
            'wind_direction': [wind_direction[guanacaste][i]],
            'lat': [lat[guanacaste][i]],
            'lon': [lon[guanacaste][i]]})
            df = pd.concat([df, df_i],ignore_index=True)

df.to_csv(f'data_{day}_{year}/data_frame.csv')