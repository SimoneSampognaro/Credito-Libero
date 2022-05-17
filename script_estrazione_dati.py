import csv
import os
with open('./waves_and_wind_parameters_dati1.csv', 'r') as file:
 reader = csv.reader(file)
 dati = [(linea[3],linea[4],linea[6]) for linea in reader]    # 3, 4 e 6 per mare, 7 e 8 per vento

file_path = './estrazioneSea.csv'
try:
    os.remove(file_path)
except OSError as e:
    print("Error: %s : %s" % (file_path, e.strerror))


with open('estrazioneSea.csv', 'w', newline='') as fileOUT:
     writer = csv.writer(fileOUT)
     for dato in dati:
       print(dato)
      # CF = 0.49*(int)dato[1]*(int)pow(dato[2],2)
     #  a= float(dato[1])
     #  b= float(dato[2])
     #  CF = 0.49 * a * b * b
     #  print(CF)
       writer.writerow(dato)
       #dato.append(0.49*dato[1]*pow(dato[2],2))

#index,lat,long,time,significant_wave_height,energy_wave_period,mean_wave_direction