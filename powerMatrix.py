from cmath import inf
import csv
import os
import numpy as nmp
import math

def ricerca_massimo(power_matrix):
    max = 0
    for riga in power_matrix:
        for casella in riga:
            if(float(casella)>max):
                max = float(casella)
    return max

def ricerca_in_matrice(altezza,periodo,power_matrix):
    x =  y = 0

    min = +inf
    for i in range(0,33):
        diff=abs(float(power_matrix[0][i])-periodo)
        if(diff<min):
              min = diff 
              x = i

    min = +inf       
    for j in range(0,27):
        diff=abs(float(power_matrix[j][0])-altezza)
        if(diff<min):
              min = diff 
              y = j
    
    if(x==0 or y==0):         
            return 0
    return float(power_matrix[y][x])


power_matrix=[]
with open('./wec_matrix.csv', 'r') as file:
 reader = csv.reader(file,delimiter=',')
 for linea in reader:
   power_matrix.append(linea)

with open('./input.csv', 'r') as file2:
    reader = csv.reader(file2,delimiter=',')
    dati = [(linea[3], float(linea[4]), float(linea[5])) for linea in reader]  # 3 tempo 4 altezza 5 periodo

risultato=[]

for dato in dati:
    casella_power_matrix = ricerca_in_matrice(dato[1],dato[2],power_matrix)
    daAggiungere=[]
    daAggiungere.append(dato[0])
    daAggiungere.append(dato[1])
    daAggiungere.append(dato[2])
    daAggiungere.append(casella_power_matrix)
    risultato.append(daAggiungere)

pMax = ricerca_massimo(power_matrix)

for dato in risultato:
    CF = dato[3] / pMax
    dato.append(CF)

file_path = './CF_sotto.csv'
try:
    os.remove(file_path)
except OSError as e:
    print("Error: %s : %s" % (file_path, e.strerror))

with open('CF_sotto.csv', 'w', newline='') as fileOUT:
     writer = csv.writer(fileOUT)
     writer.writerow(["time,significant_wave_height,energy_wave_period,mean_wave_direction,produzione(kW/m),CF"])
     for linea in risultato:
         writer.writerow(linea)
