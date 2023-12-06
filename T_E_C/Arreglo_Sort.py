# -*- coding: utf-8 -*-
"""
Created on Thu May  4 22:11:35 2023

@author: LAFB2000
"""
import numpy as np

#ordenar a través de sort
A1=np.array([13,234,234,1,43,643,7,54,0,135,12,423,21,43,-53413,2142,323,341,0,22,-12,332,33121])
print("Arreglo A1 original \n",A1)
A2=np.sort(A1)
print("Arreglo A1 ordenado \n",A2)
print("\n")

A3=np.array([[13,234,234,1,43,643,7],[54,0,135,12,423,21,43],[53413,214245,4313,41,123,212,12],[-133,3212,-3121,-31212,-231,-12334,0]])
A4=np.sort(A3)
print("Arreglo A3 original \n",A3)
print("Arreglo A3 ordenado \n",A4)
print("\n")

A5=np.array(["Francisco", "Jose", "Eduardo", "Xochitl", "Joseph", "Luis", "Bryan", "casa", "Xochimilco", "francés", "educar"])
A6=np.sort(A5)
print("Arreglo A5 original \n",A5)
print("Arreglo A5 ordenado \n",A6)
print("\n")

A7=np.array([["caja", "papel", "electricidad", "moderna"], ["Yeshua", "Osiris", "testamento", "casa"],["yeshua", "osiris", "Testamento", "Casa"], 
             ["franco", "francés", "frances", "francamente"]])
A8=np.sort(A7)
A81=np.sort(A7)
print("Arreglo A7 original \n",A7)
print("Arreglo A7 ordenado \n", A8)
print("\n")