import csv
import os
import numpy as np


tempo=[]
with open('./CF_sopra.csv', 'r') as fileTEMP:
 reader = csv.reader(fileTEMP,delimiter=',')
 for linea in reader:
    tempo = [(linea[0]) for linea in reader]




datiCFsopra=[]
with open('./CF_sopra.csv', 'r') as file:
 reader = csv.reader(file,delimiter=',')
 for linea in reader:
    datiCFsopra = [(linea[4]) for linea in reader]


datiCFsotto=[]
with open('./CF_sotto.csv', 'r') as file2:
 reader = csv.reader(file2,delimiter=',')
 for linea in reader:
    datiCFsotto = [(linea[4]) for linea in reader]


datiCFoffshoresopra=[]
with open('./offshore sopra.csv', 'r') as file3:
 reader = csv.reader(file3,delimiter=';')
 for linea in reader:
    datiCFoffshoresopra = [(linea[7].replace(",",".")) for linea in reader]


datiCFoffshoresotto=[]
with open('./offshore sotto.csv', 'r') as file4:
 reader = csv.reader(file4,delimiter=';')
 for linea in reader:
    datiCFoffshoresotto = [(linea[7].replace(",",".")) for linea in reader]

datiCFonshoresopra=[]
with open('./onshore sopra.csv', 'r') as file4:
 reader = csv.reader(file4,delimiter=';')
 for linea in reader:
    datiCFonshoresopra = [(linea[7].replace(",",".")) for linea in reader]

datiCFoonshoresotto=[]
with open('./onshore sotto.csv', 'r') as file5:
 reader = csv.reader(file5,delimiter=';')
 for linea in reader:
    datiCFoonshoresotto = [(linea[7].replace(",",".")) for linea in reader]

datiCFsolareNORD=[]
with open('./solare 1MW nord.csv', 'r') as file6:
 reader = csv.reader(file6,delimiter=';')
 for linea in reader:
    datiCFsolareNORD = [(linea[7].replace(",",".")) for linea in reader]

datiCFsolareSUD=[]
with open('./solare 1MW sud.csv', 'r') as file7:
 reader = csv.reader(file7,delimiter=';')
 for linea in reader:
    datiCFsolareSUD = [(linea[7].replace(",",".")) for linea in reader]

consumo=[]
with open('./carico elettrico.csv', 'r') as file8:
 reader = csv.reader(file8,delimiter=';')
 for linea in reader:
    consumo = [(linea[2].replace(",",".")) for linea in reader]


risultato=[]
risultato.append(["Tempo, CF wec sopra, CF wec sotto, CF OFS sopra, CF OFS sotto, CF ONS sopra, CF ONS sotto, CF sun sopra, CF sun sotto,consumo"])

for i in range(0,8760):
    daAppendere=[]
    daAppendere.append(tempo[i])
    daAppendere.append(float(datiCFsopra[i]))
    daAppendere.append(float(datiCFsotto[i]))
    daAppendere.append(float(datiCFoffshoresopra[i]))
    daAppendere.append(float(datiCFoffshoresotto[i]))
    daAppendere.append(float(datiCFonshoresopra[i]))
    daAppendere.append(float(datiCFsolareNORD[i]))
    daAppendere.append(float(datiCFsolareSUD[i]))
    daAppendere.append(float(consumo[i]))
    risultato.append(daAppendere)


file_path = './tabellaCF.csv'
try:
    os.remove(file_path)
except OSError as e:
    print("Error: %s : %s" % (file_path, e.strerror))    

with open('tabellaCF.csv', 'w', newline='') as fileOUT:
     writer = csv.writer(fileOUT)
     for linea in risultato:
         writer.writerow(linea)