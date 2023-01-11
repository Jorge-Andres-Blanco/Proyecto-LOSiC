# ¿Qué pretende generar este proyecto?
Se pretende poder obtener datos de la velocidad y dirección del viento medido por el satélite GOES-16 en Costa Rica para su comparación con las mediciones hechas en las estaciones metereológicas nacionales
## Los datos
Los datos se obtienen de la banda 2 (C02) del Advanced Baseline Imager (ABI), ya que esta banda puede detectar de mejor manera las nubes y su movimiento a menores altitudes respecto al nivel del mar.
La idea es tener un pequeño script ejecutable de bash que descargue de forma automática los datos del GOES-16 en la banda 2 de un día y año que se especifiquen como parámetros.
Posteriormente un programa hecho en Python se encarga de hacer un filtrado preliminar de los datos, seleccionando las mediciones en que se pudo obtener una velocidad y dirección válida dentro del territorio de Costa Rica. También se fitra para una presión mayor a 850 hPa ya que interesa mediciones cercanas al nivel del suelo.
Una vez con estos datos filtrados, estos se guardan como un dataframe en un archivo .csv usando la librería pandas.
#Análisis
Los datos se analizan usando un notebook de jupyter, en este se filtran más los datos a un intervalo específico dependiendo de lo que se quiera analizar. Idealmente, en este notebook se compararía los datos del GOES-16 con las mediciones hechas en tierra. 
