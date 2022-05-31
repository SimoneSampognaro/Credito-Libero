import csv
import os
import numpy as np
import openpyxl
file_excel = openpyxl.load_workbook('test.xlsx')

tempo=[]
with open('./CF_kawai_wec', 'r') as fileTEMP:
 reader = csv.reader(fileTEMP,delimiter=',')
 for linea in reader:
    tempo = [(linea[0]) for linea in reader]


datiCFsopra=[]
with open('./CF_kawai_wec', 'r') as file:
 reader = csv.reader(file,delimiter=',')
 for linea in reader:
    datiCFsopra = [(linea[4]) for linea in reader]



consumo=[]
with open('./carico elettrico.csv', 'r') as file8:
 reader = csv.reader(file8,delimiter=';')
 for linea in reader:
    consumo = [(linea[2].replace(",",".")) for linea in reader]

pMax = 76891.2000390625/1000000
risultato=[]
#risultato.append(["Tempo, CF wec sopra, CF wec sotto, CF OFS sopra,  CF OFS sotto, CF ONS sopra, CF ONS sotto, CF sun sopra, Y FV installato sopra, CF sun sotto, Y FV installato sotto, consumo"])
risultato.append(["Tempo, CF wec, produzione WEC, CF eolico, produzione EOLICO, CF FV, produzione FV, consumo elettrico, produzione diesel"])
for i in range(0,8760):
    daAppendere=[]
    daAppendere.append(tempo[i])
    daAppendere.append(float(datiCFsopra[i]))
    daAppendere.append(float(datiCFsopra[i])*pMax)
   # daAppendere.append(float(datiCFsotto[i]))
   # daAppendere.append(float(datiCFsotto[i])*pMax)
    daAppendere.append(float(datiCFoffshoresopra[i]))
    daAppendere.append(float(datiCFoffshoresopra[i])*15)
  #  daAppendere.append(float(datiCFoffshoresotto[i]))
   # daAppendere.append(float(datiCFoffshoresotto[i])*15)
    #daAppendere.append(float(datiCFonshoresopra[i]))
    #daAppendere.append(float(datiCFonshoresopra[i])*15)
    #daAppendere.append(float(datiCFoonshoresotto[i]))
    #daAppendere.append(float(datiCFoonshoresotto[i])*15)
    daAppendere.append(float(datiCFsolareNORD[i]))
    daAppendere.append(float(datiCFsolareNORD[i])*4)
    #daAppendere.append(float(datiCFsolareSUD[i]))
    #daAppendere.append(float(datiCFsolareSUD[i])*4)
    daAppendere.append(float(consumo[i]))
    #daAppendere.append(float(consumo[i])-(float(datiCFsolareNORD[i])*4)-(float(datiCFoffshoresopra[i])*15)-((float(datiCFsopra[i])*pMax)))
    daAppendere.append(float(consumo[i])-(float(datiCFoffshoresopra[i])*6))
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


countM = 0
somma = 0
sommaVarianzaSotto = 0
for linea in risultato:
      count = 0
      for dato in linea:
          if(count==8):
                print(dato)
                somma = somma + float(dato)
                sommaVarianzaSotto = sommaVarianzaSotto + pow(float(dato),2)
                countM = countM + 1
          count = count +1     
      #print(count)


media = somma/countM
mediaQuadrato =  sommaVarianzaSotto/countM

varianzaSopra = mediaQuadrato - pow(media,2)

print("Ecco la media: ",media," varianza: ",varianzaSopra)