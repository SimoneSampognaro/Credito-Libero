import csv
import os
import numpy as nmp
import math

def ricerca_in_matrice(altezza,periodo,power_matrix):
    x =  y = 0
    altezza = round(altezza,1)
    periodo = round(periodo,1)
    #for riga in power_matrix:
    for i in range(0,33):           
            if(float(power_matrix[0][i])>periodo):
                #print(power_matrix[0][i],periodo)
                x = i-1
                break
    for j in range(0,27):           
            if(float(power_matrix[j][0])>altezza):
                #print(power_matrix[j][0],altezza)
                y = j-1
                break
    #print(x,y,power_matrix[y][x])
    if(x==0 or y==0):
            return 0
    return power_matrix[y][x]


power_matrix=[]
with open('./wec_matrix.csv', 'r') as file:
 reader = csv.reader(file,delimiter=',')
 for linea in reader:
   power_matrix.append(linea)



with open('./input.csv', 'r') as file2:
    reader = csv.reader(file2,delimiter=',')
    dati = [(linea[3], float(linea[4]), float(linea[5])) for linea in reader]  # 3 tempo 4 altezza 5 periodo

risultato=[]
#print("Ecco un esempio", power_matrix[1][4])


for dato in dati:
    casella_power_matrix = ricerca_in_matrice(dato[1],dato[2],power_matrix)
    #dato.append(casella_power_matrix)
    #daAggiungere=[]
  #  daAggiungere.append(dato)
   # daAggiungere.append(casella_power_matrix)
    daAggiungere=[]
    daAggiungere.append(dato[0])
    daAggiungere.append(dato[1])
    daAggiungere.append(dato[2])
    daAggiungere.append(casella_power_matrix)
    risultato.append(daAggiungere)

for linea in risultato:
   print(linea)
#print(nmp.ceil(12.3))
#x=3.85 
#y=round(x,1)
#print(y)