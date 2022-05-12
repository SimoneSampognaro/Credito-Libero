import csv
import os
with open('./waves_and_wind_parameters_dati1.csv', 'r') as file:
 reader = csv.reader(file)
 dati = [(linea[4],linea[6]) for linea in reader]

file_path = './estrazione.csv'
try:
    os.remove(file_path)
except OSError as e:
    print("Error: %s : %s" % (file_path, e.strerror))

with open('estrazione.csv', 'w', newline='') as fileOUT:
     writer = csv.writer(fileOUT)
     for dato in dati:
       writer.writerow(dato)
   
