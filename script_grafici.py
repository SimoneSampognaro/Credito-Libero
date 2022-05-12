import seaborn
import pandas
import matplotlib.pyplot as plt
csv = pandas.read_csv(r'C:\waves_and_wind_parameters_dati1.csv')
res = seaborn.lineplot(x="Name", y="Age", data=csv)
plt.show()