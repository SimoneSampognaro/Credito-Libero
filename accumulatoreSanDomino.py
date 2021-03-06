import csv
import os
import numpy as np

def possoAccumulare(soc,effCar,dato,accumulatore):
       return ((((100-soc)/100)*accumulatore)>abs(dato)*effCar)

def hoEnergiaInPiĆ¹(dato):
    return dato<0

def socNonCento(soc):
    return soc<100

def socNonZero(soc):
    return soc>0

def possoPrelevare(soc,effScar,accumulatore,dato):
    return (((soc/100)*accumulatore)>(dato/effScar))

tempo=[]
with open('./CF_sopra.csv', 'r') as fileTEMP:
 reader = csv.reader(fileTEMP,delimiter=',')
 for linea in reader:
    tempo = [(linea[0]) for linea in reader]


sommaCFwind=0
sommaCFwec = 0
sommaProdwec = 0
sommaProdWind=0
consumoTOT = 0
socMedio = 0
prod_dieselTOT = 0

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
with open('./offshore_5MW.csv', 'r') as file3:
 reader = csv.reader(file3,delimiter=';')
 for linea in reader:
    datiCFoffshoresopra = [(linea[2].replace(",",".")) for linea in reader]


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
sommaProdsol= 0
sommaCFsol = 0
#risultato.append(["Tempo, CF wec sopra, CF wec sotto, CF OFS sopra,  CF OFS sotto, CF ONS sopra, CF ONS sotto, CF sun sopra, Y FV installato sopra, CF sun sotto, Y FV installato sotto, consumo"])
risultato.append(["Tempo, CF wec, produzione WEC, consumo elettrico, produzione diesel"])
for i in range(0,8760):
    daAppendere=[]
    daAppendere.append(tempo[i])
   # daAppendere.append(float(datiCFsopra[i]))
 #   daAppendere.append(float(datiCFsopra[i])*pMax*2)
    #daAppendere.append(float(datiCFoffshoresopra[i]))
   # Cf_sol = Cf_sol + float(datiCFsolareNORD[i])
   # daAppendere.append(float(datiCFoffshoresopra[i])*5)
    daAppendere.append(float(datiCFsolareNORD[i]))
    daAppendere.append(float(datiCFsolareNORD[i])*2)
   # sol = sol + float(datiCFsolareNORD[i])*2
    daAppendere.append(float(consumo[i]))
    daAppendere.append(float(consumo[i])-(float(datiCFsolareNORD[i])*2))
    risultato.append(daAppendere)
 #   sommaCFwind= (float(eolico[i])) + sommaCFwind
  #  sommaProdWind= (float(eolico[i])*18*8) + sommaProdWind
    consumoTOT = consumoTOT + (float(consumo[i]))
    sommaCFwec = sommaCFwec + (float(datiCFsopra[i]))
    sommaProdwec = sommaProdwec + (float(datiCFsopra[i])*pMax*2)
    sommaProdsol= sommaProdsol + (float(datiCFsolareNORD[i])*2)
    sommaCFsol = sommaCFsol + (float(datiCFsolareNORD[i]))


#print("PRODUZIONE SOLARE: ",sol)
#mediacfsol = Cf_sol / 8760
#print("MEDIA CF : ",mediacfsol)
file_path = './ModelloElettricoSanDomino.csv'
try:
    os.remove(file_path)
except OSError as e:
    print("Error: %s : %s" % (file_path, e.strerror))    

with open('2MW_PV.csv', 'w', newline='') as fileOUT:
     writer = csv.writer(fileOUT)
     for linea in risultato:
         writer.writerow(linea)

energia=[]
diesel=[]

for linea in risultato:
      count = 0
      for dato in linea:
          if(count==4):
                energia.append(dato)
          count = count + 1

soc = 0
effCar = 0.975
effScar = 0.975
accumulatore = 10 # suppongo 100 MWh
maxdelta=0
prec = 0
totale = 0

for dato in energia:
    prod_diesel = 0
    if(hoEnergiaInPiĆ¹(dato)): 
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
       # print("ecco prec: ",prec,"ecco soc: ",soc,"ecco maxDelta: ",maxdelta)
    socMedio = socMedio + soc
    prec = soc
    totale = totale + prod_diesel
    diesel.append(prod_diesel)

print(maxdelta)

file_path = './richiestaDiesel.csv'
try:
    os.remove(file_path)
except OSError as e:
    print("Error: %s : %s" % (file_path, e.strerror))    


with open('richiestaDieselSanDomino.csv', 'w', newline='') as fileOUT:
     writer = csv.writer(fileOUT)
     writer.writerows(map(lambda x: [x], diesel))

"""
with open('soc.csv', 'w', newline='') as fileOUT2:
     writer = csv.writer(fileOUT2)
     for linea in socLista:
       writer.writerow(linea)
       """
"""
soc = 0
for dato in energia:
    prod_diesel=0
    if(dato<0):
        if(soc<100):
            if(((100-soc)/100)*accumulatore>"""

print("Necessario diesel:",totale)

costoimpianti = 883 * 1000 + 7611 * 1000 * pMax * 2
print("Costo impianti :",costoimpianti)

costoAccumulatore = 525000 * maxdelta + 160000 * accumulatore 

print("Costo accumulatore : ",costoAccumulatore)
costodiesel = totale * 390


costototale = costoAccumulatore + costoimpianti + costodiesel

print("Costo totale :",costototale)

sommaCFsol= sommaCFsol/8760
socMedio = socMedio/8760
sommaCFwec = sommaCFwec/8760

print(sommaCFwec)
print(sommaProdwec)

print("CF_sun medio: ",sommaCFsol,"prodTOT_sol: ",sommaProdsol,"consumoTOT: ",consumoTOT,"socMedio: ",socMedio,"ProdDieselTOT: ",totale)