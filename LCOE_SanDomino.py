import csv
import os


# eolico offshore
# CF calcolato tramite Global Wind Atlas = 0.32

CF = 0.32
energiaProdotta = CF * 0.9 * 8760 * 6

t = 25 #tempo di vita
r = 0.025 #discount ratio

capex = 3185 * 1000 * 6

opex = 100 * 1000 * 6

opexTot = 0
energiaProdottaTot = 0

for i in range(0,t):
      opexTot = opexTot + (opex/pow(1+r,i))
      energiaProdottaTot = energiaProdottaTot + (energiaProdotta/pow(1+r,i))

LCOE_Wind = (capex+opexTot)/energiaProdottaTot

print("Energia prodotta Wind: ",round(energiaProdotta,0),"MWh")
print("Ecco LCOE Eolico Offshore: ",round(LCOE_Wind,0)," USD/MWh")



energiaProdottaWec=0
datiWEC=[]
sommaCF=0
pMax = 76891.2000390625/1000000
with open('./CF_sopra.csv', 'r') as file1:
 reader = csv.reader(file1,delimiter=',')
 for linea in reader:
    datiWEC = [(linea[4]) for linea in reader] 

for dato in datiWEC:
    #print(dato)
    energiaProdottaWec = energiaProdottaWec + float(dato)*pMax
    sommaCF = sommaCF + float(dato)

CF_medio = sommaCF / 8760

print("Energia prodotta WEC: ",round(energiaProdottaWec,0),"MWh, il CF medio è: ",CF_medio)

r = 0.025 #discount ratio
capex_wec = 7611 * 1000 * pMax

opex_wec = (capex_wec*3)/100 # opex è il 3% del capex

opexTot = 0
energiaProdottaTot = 0

t = 20 #tempo di vita

for i in range(0,t):
      opexTot = opexTot + (opex_wec/pow(1+r,i))
      energiaProdottaTot = energiaProdottaTot + (energiaProdottaWec/pow(1+r,i))

LCOE_wec = (capex_wec+opexTot)/energiaProdottaTot

print("Ecco LCOE Wec: ",round(LCOE_wec,0)," USD/MWh")


# Global Solar Atlas 1799.2 KWh/m^2

energiaProdottaFV  = 1496 # MWh
#(1799 * 20000) / 1000 # rettangolo da 100 x 200 m

r = 0.025 #discount ratio
capex_FV = 883 * 1000 # considero 2 MWh di solare installato 
opex_FV = 14 * 1000 

opexTot = 0
energiaProdottaTot = 0

t = 25 #tempo di vita

for i in range(0,t):
      opexTot = opexTot + (opex_FV/pow(1+r,i))
      energiaProdottaTot = energiaProdottaTot + (energiaProdottaFV/pow(1+r,i))

LCOE_FV = (capex_FV+opexTot)/energiaProdottaTot

print("Energia prodotta FV: ",round(energiaProdottaFV,0),"MWh")
print("Ecco LCOE FV: ",round(LCOE_FV,0)," USD/MWh")



