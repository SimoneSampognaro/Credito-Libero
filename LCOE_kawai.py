import csv
import os


# eolico offshore
# CF calcolato tramite Global Wind Atlas = 0.51 nord

CF = 0.51
energiaProdotta = CF * 0.9 * 8760 * 18

t = 25 #tempo di vita
r = 0.025 #discount ratio

capex_wind = 4310 * 1000 * 18

opex_wind = (capex_wind*3)/100

opexTot = 0
energiaProdottaTot = 0

for i in range(0,t):
      opexTot = opexTot + (opex_wind/pow(1+r,i))
      energiaProdottaTot = energiaProdottaTot + (energiaProdotta/pow(1+r,i))

LCOE_Wind = (capex_wind+opexTot)/energiaProdottaTot

print("Energia prodotta Wind: ",round(energiaProdotta,0),"MWh")
print("Ecco LCOE Eolico Offshore: ",round(LCOE_Wind,0)," USD/MWh")



energiaProdottaWec=0
datiWEC=[]
sommaCF=0
pMax = 76891.2000390625/1000000
with open('./wecK.csv', 'r') as file1:
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
capex_wec = 6164 * 1000  * pMax 

opex_wec = (capex_wec*3)/100 # opex è il 3% del capex

opexTot = 0
energiaProdottaTot = 0

t = 20 #tempo di vita

for i in range(0,20):
      opexTot = opexTot + (opex_wec/pow(1+r,i))
      energiaProdottaTot = energiaProdottaTot + (energiaProdottaWec/pow(1+r,i))

LCOE_wec = (capex_wec+opexTot)/energiaProdottaTot

print("Ecco LCOE Wec: ",round(LCOE_wec,0)," USD/MWh")




