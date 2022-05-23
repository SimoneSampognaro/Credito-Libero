import seaborn
import pandas
import matplotlib.pyplot as plt
csv = pandas.read_csv(r'./estrazione.csv')
res = seaborn.lineplot(x="significant_wave_height", y="mean_wave_direction", data=csv)
plt.show()

 #daAppendere.append(tempo[i])
 #   daAppendere.append(float(datiCFsopra[i]))
  #  daAppendere.append(float(datiCFsotto[i]))
   # daAppendere.append(float(datiCFoffshoresopra[i]))
   # daAppendere.append(float(datiCFoffshoresotto[i]))
    #daAppendere.append(float(datiCFonshoresopra[i]))
    #daAppendere.append(float(datiCFsolareNORD[i]))
    #daAppendere.append(float(datiCFsolareSUD[i]))
    #daAppendere.append(float(consumo[i]))