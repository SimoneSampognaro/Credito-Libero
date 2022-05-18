import csv
import os
matrice=[]
with open('./wec_matrix.csv', 'r') as file:
 reader = csv.reader(file,delimiter=',')
 for linea in reader:
   matrice.append(linea)

