# pacchetti da installare
import netCDF4 as nec
import pandas as pd
import os
import xarray as xr

# inserisco il nome del file contenente i dati
namedatafile = 'kawai1.nc'

# leggo il file netcdf
data = nec.Dataset(r'kawai1.nc')

# print dei nomi delle variabili presenti nel file
print(data.variables.keys()) 

#### TO DO: leggere il nome delle variabili riferite alle componenti della velocitÃ  del vento a 100 m

# leggo il file netcdf come un dataset
ds_data = xr.open_dataset(namedatafile)

#### TO DO: estrarre dal file le componenti della velocitÃ  del vento a 100 m
#### TO DO: calcolare la risultante della velocitÃ  del vento a 100 m

# converto il dataset in un dataframe
df_data = ds_data.to_dataframe()
# resetto gli indici del dataframe
df_data.reset_index(inplace=True)

# creo la tabella "waves_and_wind_parameters"
df_data_table = pd.DataFrame()
# estraggo dal file i parametri di interesse e il assegno alle colonne della tabella
df_data_table["lat"] = df_data["latitude"]
df_data_table["long"] = df_data["longitude"]
df_data_table["time"] = df_data["time"]
df_data_table["significant_wave_height"] = df_data["swh"]
df_data_table["energy_wave_period"] = df_data["mwp"]
df_data_table["mean_wave_direction"] = df_data["mwd"]
df_data_table["100m_ucomponent_wind"] = df_data["u100"]
df_data_table["100m_vcomponent_wind"] = df_data["v100"]
#### TO DO: aggiungere la parte di codice per all'assegnazione della risultante della velocitÃ  del vento ad una colonna della tabella

df_data_table.index.names=['index']
df_data_table.to_csv("kawai1OUT.csv")