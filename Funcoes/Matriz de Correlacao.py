# importando as bibliotecas 
import sklearn 
import csv
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sn



redwine = pd.read_csv('/ICA/Datas/winequality-red.csv', sep= ';')
whitewine =  pd.read_csv('/ICA/Datas/winequality-white.csv', sep = ';')

redwine.isnull()
whitewine.isnull()
correlacao1 = redwine.corr()
correlacao2= whitewine.corr()
sn.heatmap(correlacao1, annot=True)
plt.show()

sn.heatmap(correlacao2, annot=True)
plt.show()

#scatter plots
#juntar os vinhos e depois fazer mais uma coluna e depois 
#scatter plots evidenciando qual o vinho branco e o vermelho faz mais uma matriz pra largar de ser besta
#boxplot de cada um dos preditores 
