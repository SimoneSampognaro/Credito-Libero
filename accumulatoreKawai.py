import csv
import os
import numpy as np

def possoAccumulare(soc,effCar,dato,accumulatore):
       return ((100-soc)*accumulatore>(abs(dato)*effCar))

def hoEnergiaInPiù(dato):
    return dato<0

def socNonCento(soc):
    return soc<100

def socNonZero(soc):
    return soc>0

def possoPrelevare(soc,effScar,accumulatore,dato):
    return ((soc*accumulatore)>(dato/effScar))


tempo=[]
with open('./wecK.csv', 'r') as fileTEMP:
 reader = csv.reader(fileTEMP,delimiter=',')
 for linea in reader:
    tempo = [(linea[0]) for linea in reader]

wec=[]
with open('./wecK.csv', 'r') as file1:
 reader = csv.reader(file1,delimiter=',')
 for linea in reader:
    wec = [(linea[4]) for linea in reader]

eolico=[]
with open('./offshore_kauai.csv', 'r') as file1:
 reader = csv.reader(file1,delimiter=';')
 for linea in reader:
    eolico = [(linea[8].replace(",",".")) for linea in reader]

consumo=[]
with open('./caricokawai.csv', 'r') as file8:
 reader = csv.reader(file8,delimiter=';')
 for linea in reader:
    consumo = [(linea[1].replace(",",".")) for linea in reader]

pMax = 76891.2000390625/1000000
risultato=[]

risultato.append(["Tempo, CF wec, produzione WEC, CF eolico offshore, produzione EOLICO offshore, consumo elettrico, produzione diesel"])
for i in range(0,8760):
    daAppendere=[]
    daAppendere.append(tempo[i])
    daAppendere.append(float(wec[i]))
    daAppendere.append(float(wec[i])*pMax)
    daAppendere.append(float(eolico[i]))
    daAppendere.append(float(eolico[i])*18)
    daAppendere.append(float(consumo[i])*449798)
    daAppendere.append((float(consumo[i])*449798)-((float(wec[i])*pMax)*2)-((float(eolico[i])*18)*5))
    #print("ecco il consumo",consumo[i],"ecco cosa avanza",(float(consumo[i])-(float(wec[i])*pMax)))
    risultato.append(daAppendere)


file_path = './ModelloElettricoKawai.csv'
try:
    os.remove(file_path)
except OSError as e:
    print("Error: %s : %s" % (file_path, e.strerror))    

with open('ModelloElettricoKawai.csv', 'w', newline='') as fileOUT:
     writer = csv.writer(fileOUT)
     for linea in risultato:
         writer.writerow(linea)


energia=[]
diesel=[]

for linea in risultato:
      count = 0
      for dato in linea:
          if(count==6):
                energia.append(dato)
                #print(dato)
          count = count + 1

soc = 0
effCar = 0.975
effScar = 0.975
accumulatore = 100 # suppongo 100 MWh
maxdelta=0
prec = 0

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

    if(((abs(soc-prec)/100)*accumulatore)>maxdelta):
        maxdelta = ((abs(soc-prec)/100)*accumulatore)
    prec = soc
    diesel.append(prod_diesel)

print(maxdelta)

file_path = './richiestaDieselKawai.csv'
try:
    os.remove(file_path)
except OSError as e:
    print("Error: %s : %s" % (file_path, e.strerror))    

with open('richiestaDieselKawai.csv', 'w', newline='') as fileOUT:
     writer = csv.writer(fileOUT)
     writer.writerows(map(lambda x: [x], diesel))
