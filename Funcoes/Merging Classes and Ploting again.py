import sklearn 
import csv
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sn
import plotly.express as px

redwine = pd.read_csv('/ICA/Datas/winequality-red.csv', sep= ';')
whitewine =  pd.read_csv('/ICA/Datas/winequality-white.csv', sep = ';')


redwine.isnull()
whitewine.isnull()
redwine.loc[:, 'Tipo'] = 1
whitewine.loc[:, 'Tipo'] = 2
print(redwine)
print(whitewine)
mergewine= pd.concat([redwine, whitewine]).reset_index(drop=True)
print(mergewine)



sn.pairplot(mergewine, kind="scatter", hue='Tipo', markers=["o", "o"], palette="Set2")
plt.savefig('mergewinescatterplotbonitinho.png', format='png')
plt.show()
