import csv
with open('./waves_and_wind_parameters_dati1.csv', 'r') as file:
 reader = csv.reader(file, delimiter=";")
 for row in reader:
        print(row)