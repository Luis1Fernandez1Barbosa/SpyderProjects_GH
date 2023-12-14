# -*- coding: utf-8 -*-
"""
Created on Fri May  5 07:27:23 2023

@author: Alumno-39-203
"""

import pandas as pd

dict1 = {'Nombre': pd.Series(['Feria de Cepillin','En el radio cochinero', 'Pollito pio', 'Quiero ver amanecer','Himno'],
          index=[1, 2, 3, 4,5]),
         'Calificacion': pd.Series([10, 7, 8, 5000],index=[1, 2, 4,5]),
         'Reproducciones': pd.Series([10, 20, 15, 1], index=[2, 3, 4,5])}

 
df = pd.DataFrame(dict1, index=[1, 2, 3, 4,5])
print(df)
print("------------------------------------------------------------------")

#Evalua el dataframe y lo arroja como arreglo
df1=df.values
print(df1)
print("------------------------------------------------------------------")

#Busca el #2 de la columna 0
df12=df.values[2,0]
print(df12)
print("------------------------------------------------------------------")


df2=df.index
print(df2)
print("------------------------------------------------------------------")

#Busca la localización 3 con respecto a index de la primera columna "Nombre".
df4=df.loc[3]
print(df4)
print("------------------------------------------------------------------")

df = pd.DataFrame(dict1, index=[1, 2, 3, 4,5])
#elimina todo lo de NaN
df5=df.dropna()
print(df5)
print("------------------------------------------------------------------")

#agrega elemento a NaN
df ['Calificacion'].fillna(10,inplace=True)
df ['Reproducciones'].fillna(10,inplace=True)
df ['Reproducciones'].fillna(10,inplace=True)

print(df)
print("------------------------------------------------------------------")
#promedio
meanC=df['Calificacion'].mean()
print(meanC)
meanR=df['Reproducciones'].mean()
print(meanR)
print("------------------------------------------------------------------")

#mediana
medianC=df['Calificacion'].median()
print(medianC)
medianR=df['Reproducciones'].median()
print(medianR)
print("------------------------------------------------------------------")

#moda
modeC=df['Calificacion'].mode()
print(modeC)
modeR=df['Reproducciones'].mode()
print(modeR)
