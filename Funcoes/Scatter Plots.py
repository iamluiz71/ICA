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

sn.pairplot(redwine, kind='reg')
plt.savefig('redwineregression.png', format='png')
plt.show()  

sn.pairplot(whitewine, kind='reg')
plt.savefig('whitewineregrssion.png', format='png')
plt.show()  
