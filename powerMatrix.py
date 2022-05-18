import csv
import os
matrice=[]
with open('./wec_matrix.csv', 'r') as file:
 reader = csv.reader(file,delimiter=',')
 for linea in reader:
   matrice.append(linea)

with open('./input.csv', 'r') as file2:
    reader = csv.reader(file2,delimiter=',')
    dati = [(linea[3], float(linea[4]), float(linea[5])) for linea in reader]  # 3 tempo 4 altezza 5 periodo

