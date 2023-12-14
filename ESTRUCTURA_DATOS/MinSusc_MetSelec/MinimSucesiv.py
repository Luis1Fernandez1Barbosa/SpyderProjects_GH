# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 19:25:37 2022

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
ventana.title("Método de Ordenamiento")
ventana.geometry("900x880")

def InsetarD ():
    i=Entra.get()
    if (i=='' or i==' ' or i=='  ' or i=='   '):
        ventana=Tk()
        ventana.title("¡¡¡ERROR!!!")
        ventana.geometry("300x100")    
        Label(ventana, text='¡¡INSERTE UN DATO!!').pack()
        return Entra.set('')
    else:
        ListN.append(int(i))
        cLis.insert(1.0, "\n")
        for i in ListN:
            print (ListN)
            cLis.insert(1.0,ListN)
            return Entra.set('')

"""----------------------------------------------------------------"""

def MinSusc():
    cLis.delete(1.0,'end')    
    long=len(ListN)
    cLis.insert(1.0, '\n')
    cLis.insert(1.0, ListN)
    cLis.insert(1.0, 'Arreglo Inicial: ')
    cLis.insert(3.0, '****Proceso de abajo a arriba****\n')
    for i in range(long-1):
        print(ListN)
        menor=i
        print('El indice actual a comparar es ', menor)
        cLis.insert(4.0, '\n')
        cLis.insert(4.0, menor)
        cLis.insert(4.0, '-------------------------------')
        cLis.insert(4.0, '\n')
        cLis.insert(4.0, menor)
        cLis.insert(4.0, '\nIndice actual a comparar: ')
        for j in range(i+1, long):
            if (ListN[j] < ListN[menor]):
                menor=j
                print('Recorriendo. Es menor el índice: ', menor)
                cLis.insert(5.0, '\n')
                cLis.insert(5.0, menor)
                cLis.insert(5.0, '\nEs menor el índice: ')  
                
        temp= ListN[menor]
        ListN[menor]=ListN[i]
        ListN[i]= temp
        print('Cambio el elemento: ', ListN[menor], ' por el elemento: ', ListN[i])
        cLis.insert(6.0, '\n')
        cLis.insert(6.0, ListN[i])
        cLis.insert(6.0, ' por el elemento: ')
        cLis.insert(6.0, ListN[menor])
        cLis.insert(6.0, 'Cambio el elemento: ')
       
    print('Arreglo final: ', ListN)
    cLis.insert(2.0, '\n\n')
    cLis.insert(2.0, ListN)
    cLis.insert(2.0, 'Arreglo Ordenado: ')
"""------------------------------------------------------------------"""

def Insertar1 ():
    ListN = np.random.randint(low=-99999, high=99999, size=1000).tolist()
    cLis.delete(1.0,'end') 
    cLis.insert(1.0, "Lista Original Aleatoria:\n")
    cLis.insert(2.0, ListN)
    cLis.insert(3.0,"\n")
    cLis.insert(3.0,"----------------------------------------------------------")
    long =len(ListN)
    cLis.insert(5.0, "Hora Inicio: "+ Ahora.strftime('%H:%M:%S.%f\n'))
    #Bucle
    for i in range(long-1):
        menor=i
        for j in range (i+1,long):
            if ListN[j]<ListN[menor]:
                menor=j
        temp=ListN[menor]
        ListN[menor]=ListN[i]
        ListN[i]=temp
    cLis.insert(4.0,ListN)
    cLis.insert(4.0,"Lista Ordenada: \n")
    cLis.insert(6.0, "\nHora Final: "+ Ahora.strftime('%H:%M:%S.%f\n'))
    cLis.insert(6.0,"----------------------------------------------------------")
    cLis.insert(7.0, statistics.median(ListN))
    cLis.insert(7.0, "Mediana: ")
    cLis.insert(8.0,"\n")
    v=i+1
    c=j+1
    cLis.insert(9.0, '# de Vueltas: ')
    cLis.insert(9.0, v)
    cLis.insert(9.0, '\n')
    cLis.insert(9.0, c)
    cLis.insert(9.0,'# de Comparaciones: ')
    return ListN

frm.pack(fill="both", expand="True")
frm.config(bg="red")
frm.config(width="450", height="580")
frm.config(bd=30)
frm.config(relief="sunken")
frm.config(cursor="pirate")
ListN=[]

Label(frm,text=Ahora.strftime('%d/%m/%Y\n%H:%M:%S')).grid(row=0,column=0)
Label(frm,text='MINIMOS SUCESIVOS').grid(row=0,column=1)
Label(frm, text="Inserte dato : ").grid(row=1, column=0, sticky="e", pady="3")

Entra=StringVar() 
ctxt=Entry(frm, textvariable=Entra).grid(row=1,column=1)

BtnIns=Button(frm, text='Insertar Dato', command=InsetarD)
BtnIns.grid(row=2,column=1, sticky='s')
BtnIns=Button(frm, text='Ordenar', command=MinSusc)
BtnIns.grid(row=2,column=2, sticky='s')
BtnIns=Button(frm, text='RANDOM', command=Insertar1)
BtnIns.grid(row=2,column=0, sticky='s')

cLis=Text(frm, width=105,height=45)
cLis.grid(row=3,column=0, columnspan=3)
ventana.mainloop()