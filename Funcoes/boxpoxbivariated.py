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
mergewine= pd.concat([redwine, whitewine]).reset_index(drop=True)
print(mergewine)


sn.boxplot(y='fixed acidity', x='quality', data=mergewine)
plt.savefig('fixedacidityboxplot.png', format='png')
plt.show() 

sn.boxplot(y='volatile acidity', x='quality', data=mergewine)
plt.savefig('volatileadidityboxplot.png', format='png')
plt.show() 


sn.boxplot(y='citric acid', x='quality', data=mergewine)
plt.savefig('citricacidboxplot.png', format='png')
plt.show() 


sn.boxplot(y='residual sugar', x='quality', data=mergewine)
plt.savefig('residualsugarboxplot.png', format='png')
plt.show() 


sn.boxplot(y='chlorides', x='quality', data=mergewine)
plt.savefig('chloridesboxplot.png', format='png')
plt.show() 


sn.boxplot(y='free sulfur dioxide', x='quality', data=mergewine)
plt.savefig('freesulfurdioxideboxplot.png', format='png')
plt.show() 


sn.boxplot(y='total sulfur dioxide', x='quality', data=mergewine)
plt.savefig('totalsulfurdioxideboxplot.png', format='png')
plt.show() 


sn.boxplot(y='density', x='quality', data=mergewine)
plt.savefig('densityboxplot.png', format='png')
plt.show() 


sn.boxplot(y='pH', x='quality', data=mergewine)
plt.savefig('pHboxplot.png', format='png')
plt.show() 


sn.boxplot(y='sulphates', x='quality', data=mergewine)
plt.savefig('sulphatesboxplot.png', format='png')
plt.show() 


sn.boxplot(y='alcohol', x='quality', data=mergewine)
plt.savefig('alcoholboxplot.png', format='png')
plt.show() 




