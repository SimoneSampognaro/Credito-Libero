import seaborn
import pandas
import matplotlib.pyplot as plt
csv = pandas.read_csv(r'./estrazione.csv')
res = seaborn.lineplot(x="significant_wave_height", y="mean_wave_direction", data=csv)
plt.show()