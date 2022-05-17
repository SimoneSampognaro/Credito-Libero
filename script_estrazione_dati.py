import csv
import os
with open('./waves_and_wind_parameters_dati2.csv', 'r') as file:
 reader = csv.reader(file)
 dati = [(linea[4],linea[6]) for linea in reader]    # 4 e 6 per mare, 7 e 8 per vento

file_path = './estrazioneSea.csv'
try:
    os.remove(file_path)
except OSError as e:
    print("Error: %s : %s" % (file_path, e.strerror))

with open('estrazioneSea.csv', 'w', newline='') as fileOUT:
     writer = csv.writer(fileOUT)
     for dato in dati:
       writer.writerow(dato)
   
