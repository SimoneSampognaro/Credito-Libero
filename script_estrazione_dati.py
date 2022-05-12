import csv
with open('./waves_and_wind_parameters_dati1.csv', 'r') as file:
 reader = csv.reader(file, delimiter=";")
 #for row in reader:
     #   print(row)

['significant_wave_height','mean_wave_direction']

dati=[(linea[4],linea[6]) for linea in reader if linea[4]!="" and linea[6] != ""]
for riga in dati:
       print(riga)