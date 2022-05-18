import csv
import os
with open('./(sopra) N42,21 E15,49 S42,11 W15,39.csv', 'r') as file:
 reader = csv.reader(file)
 dati = [(linea[3],linea[4],linea[5]) for linea in reader]    # 3, 4 e 6 per mare, 7 e 8 per vento

file_path = './DatiSopra.csv'
try:
    os.remove(file_path)
except OSError as e:
    print("Error: %s : %s" % (file_path, e.strerror))

dati.pop(0)

with open('DatiSopra.csv', 'w', newline='') as fileOUT:
     writer = csv.writer(fileOUT)
     writer.writerow(["significant_wave_height,energy_wave_period,mean_wave_direction,potenza(kW/m)"])
     for dato in dati:
      # print(dato)
      # CF = 0.49*(int)dato[1]*(int)pow(dato[2],2)
       a= float(dato[1]) # wave height
       b= float(dato[2]) # wave period
       CF = 0.49 * b * a * a
       writer.writerow([dato,CF])
       #dato.append(0.49*dato[1]*pow(dato[2],2))

#index,lat,long,time,significant_wave_height,energy_wave_period,mean_wave_direction