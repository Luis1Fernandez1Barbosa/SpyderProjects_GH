# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 02:58:43 2022

@author: LAFB2000
"""
from tkinter import *
import datetime

"""------------------------------------------"""
 
matriz = [[i]*2 for i in range(3)]
def print_r(matriz):
	for fila in matriz:
		print(fila)

def transpuesta(matriz):
	reng = len (matriz)
	colm = len (matriz[0])
	return [[matriz [j][i] for j in range(reng)] for i in range(colm)]

print ("Original: ")
print_r (matriz)
print("Transpuesta: ")
print_r(transpuesta(matriz))




def transpuesta_1(matriz):
	return [[matriz [j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

def transpuesta_2(ListN):
	return [[ListN [j][i] for j in range(len(ListN))] for i in range(len(ListN[0]))]

mat_1=[[1,2,3],[4,5,6]]

print ("Original: ",mat_1)
matriz_Res=transpuesta_1(mat_1)
print("Transpuesta: ", matriz_Res)
