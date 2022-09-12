#Importando bibliotecas
import numpy as np 
import pandas as pd 
import seaborn as sn

#lendo os arquivos
redwine = pd.read_csv('/ICA/Datas/winequality-red.csv', sep= ';')
whitewine =  pd.read_csv('/ICA/Datas/winequality-white.csv', sep = ';')

#"tratando"
redwine.isnull()
whitewine.isnull()

#colocando mais uma coluna em cada um deles pra indicar o tipo
redwine.loc[:, 'Tipo'] = 1
whitewine.loc[:, 'Tipo'] = 2


#juntando
mergewine= pd.concat([redwine, whitewine]).reset_index(drop=True)
print(mergewine)