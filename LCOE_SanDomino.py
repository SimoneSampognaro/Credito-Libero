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

LCOE = (capex+opexTot)/energiaProdottaTot

print("Ecco LCOE Eolico Offshore: ",round(LCOE,0)," USD/MWh")



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
capex_wec = 1870 * 1000 * pMax

opex_wec = (capex_wec*3)/100 # opex è il 3% del capex

opexTot = 0
energiaProdottaTot = 0

t = 20 #tempo di vita

for i in range(0,t):
      opexTot = opexTot + (opex_wec/pow(1+r,i))
      energiaProdottaTot = energiaProdottaTot + (energiaProdottaWec/pow(1+r,i))

LCOE_wec = (capex_wec+opexTot)/energiaProdottaTot

print("Ecco LCOE Wec: ",round(LCOE_wec,0)," USD/MWh")
