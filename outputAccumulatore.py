import csv
import os
import numpy as np

def possoAccumulare(soc,effCar,dato,accumulatore):
       return ((100-soc)*accumulatore<(abs(dato)*effCar))

def hoEnergiaInPiù(dato):
    return dato<0

def socNonCento(soc):
    return soc<100

def socNonZero(soc):
    return soc>0

def possoPrelevare(soc,effScar,accumulatore,dato):
    return ((soc*accumulatore)>(dato/effScar))

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
    daAppendere.append(float(consumo[i])-(float(datiCFsopra[i])*pMax))
    risultato.append(daAppendere)



energia=[]
diesel=[]

for linea in risultato:
      count = 0
      for dato in linea:
          if(count==8):
                energia.append(dato)
          count = count + 1

soc = 0
effCar = 0.8
effScar = 0.8
accumulatore = 800 # suppongo 800 MWh

for dato in energia:
    prod_diesel = 0
    if(hoEnergiaInPiù(dato)): 
      if(socNonCento(soc)):
         if(possoAccumulare(soc,effCar,dato,accumulatore)):
             soc = soc + ((abs(dato)*effCar*100)/accumulatore)
         else:
             soc = 100
    else:
       if(socNonZero(soc)):
           if(possoPrelevare(soc,effScar,accumulatore,dato)):
               soc = soc - ((dato*100)/accumulatore*effScar)
           else:
                soc = 0
                prod_diesel = dato - (soc*accumulatore*effScar)
       else:
           prod_diesel = dato
    #print(soc)
    diesel.append(prod_diesel)



file_path = './richiestaDiesel.csv'
try:
    os.remove(file_path)
except OSError as e:
    print("Error: %s : %s" % (file_path, e.strerror))    

with open('richiestaDiesel.csv', 'w', newline='') as fileOUT:
     writer = csv.writer(fileOUT)
     writer.writerows(map(lambda x: [x], diesel))