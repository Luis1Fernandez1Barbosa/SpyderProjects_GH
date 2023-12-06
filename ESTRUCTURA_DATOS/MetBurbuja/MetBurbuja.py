# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 18:05:04 2022

@author: LAFB2000
"""
from tkinter import *
import datetime
import numpy as np
import statistics 
import random

Ahora=datetime.datetime.now()
print(Ahora.strftime('%d/%m/%Y\n%H:%M:%S'))

ventana=Tk()
frm=Frame()
ventana.title("METODO DE BURBUJA")
ventana.geometry("1700x1000")

ListM=[]

def Insertar1 ():
    ListM = np.random.randint(low=0, high=99999, size=1000).tolist()
    cLis.insert(1.0, "Lista Original Aleatoria:\n")
    cLis.insert(2.0, ListM)
    cLis.insert(3.0,"\n")
    cLis.insert(3.0,"----------------------------------------------------------")
    long =len(ListM)-1
    cLis.insert(5.0, "Hora Inicio: "+ Ahora.strftime('%H:%M:%S.%f\n'))
    #Bucle
    for i in range(0,long):
        for j in range (0,long):
            if ListM[j]>ListM[j+1]:
                Lx=ListM[j]
                ListM[j]=ListM[j+1]
                ListM[j+1]=Lx
    cLis.insert(4.0,ListM)
    cLis.insert(4.0,"Lista Ordenada: \n")
    cLis.insert(6.0, "\nHora Final: "+ Ahora.strftime('%H:%M:%S.%f\n'))
    cLis.insert(6.0,"----------------------------------------------------------")
    cLis.insert(7.0, statistics.median(ListM))
    cLis.insert(7.0, "Mediana: ")
    cLis.insert(8.0,"\n")
    v=i+1
    c=j+1
    cLis.insert(9.0, '# de Vueltas: ')
    cLis.insert(9.0, v)
    cLis.insert(9.0, '\n')
    cLis.insert(9.0, c)
    cLis.insert(9.0,'# de Comparaciones: ')
    return ListM

#VENTANA

frm.pack(fill="both", expand="True")
frm.config(bg="red")
frm.config(width="350", height="480")
frm.config(bd=30)
frm.config(relief="sunken")
frm.config(cursor="pirate")


Label(frm,text=Ahora.strftime('%d/%m/%Y\n%H:%M:%S')).grid(row=0,column=0)
Label(frm,text='LISTA DE NUMEROS').grid(row=0,column=1, columnspan=3) 
BtnIns=Button(frm, text='Crear y Ordenar\nLista Random (1000)', command=Insertar1)
BtnIns.grid(row=2,column=1, sticky='s')
cLis=Text(frm, width=205, height=50)
cLis.grid(row=3,column=0, columnspan=3)
ventana.mainloop()
