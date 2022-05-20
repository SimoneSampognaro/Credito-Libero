from cmath import inf
import csv
import os
import numpy as nmp
import math

dati=[]
with open('./CF_sopra.csv', 'r') as file:
 reader = csv.reader(file,delimiter=',')
 for linea in reader:
    dati.append(linea)
    #print(linea)

dati.pop(0)
CF_sopra=[]
for linea in dati:
      CF_sopra.append(linea[4])

dati2=[]
with open('./CF_sotto.csv', 'r') as file2:
 reader2 = csv.reader(file2,delimiter=',')
 for linea in reader2:
    dati2.append(linea)
    #print(linea)

dati2.pop(0)
CF_sotto=[]
for linea in dati2:
      CF_sotto.append(linea[4])
      print(linea[4])