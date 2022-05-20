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
      #print(linea[4])

somma = 0
count = 0
sommaVarianzaSopra= 0

for dato in CF_sopra:
    somma = somma + float(dato)
    sommaVarianzaSopra = sommaVarianzaSopra + pow(float(dato),2)
    count = count + 1

mediaSopra = somma/count
mediaQuadratoSopra =  sommaVarianzaSopra/count

somma = 0
count = 0
sommaVarianzaSotto = 0

for dato in CF_sotto:
    somma = somma + float(dato)
    sommaVarianzaSotto = sommaVarianzaSotto + pow(float(dato),2)
    count = count + 1

mediaSotto = somma/count
mediaQuadratoSotto =  sommaVarianzaSotto/count

varianzaSopra = mediaQuadratoSopra - pow(mediaSopra,2)
varianzaSotto = mediaQuadratoSotto - pow(mediaSotto,2)

print("Ecco le medie, sopra: ",mediaSopra," sotto: ",mediaSotto)


print("Ecco le varianze, sopra: ",varianzaSopra," sotto: ",varianzaSotto)

# Sopra è meglio !!