import csv
import os
with open('./waves_and_wind_parameters_dati1.csv', 'r') as file:
 reader = csv.reader(file)
 dati = [(linea[4],linea[6]) for linea in reader]
 #for dato in dati:
  #      print(dato)
 #for row in reader:
    #   print(row)

#['significant_wave_height','mean_wave_direction']

#dati=[(linea[4],linea[6]) for linea in reader if linea[4]!="" and linea[6] != ""]
#for riga in dati:
   #    print(riga)

file_path = './estrazione.csv'
try:
    os.remove(file_path)
except OSError as e:
    print("Error: %s : %s" % (file_path, e.strerror))

with open('estrazione.csv', 'w', newline='') as fileOUT:
     writer = csv.writer(fileOUT)
    # writer.writerow(['significant_wave_height','mean_wave_direction'])
     for dato in dati:
       writer.writerow(dato)
   
