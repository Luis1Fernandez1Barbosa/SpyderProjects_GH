# -*- coding: utf-8 -*-
"""
Created on Wed May 11 22:13:21 2022
@author: LAFB2000
"""
from random import randint
from time import time
from tkinter import *
import datetime

Ahora=datetime.datetime.now()
print(Ahora.strftime('%d/%m/%Y\n%H:%M:%S'))

ventana=Tk()
frm=Frame()
ventana.title("Algoritmos de Ordenamiento")
ventana.geometry("680x580")

def crearArreglo (size=200, max=500):
    return [randint(0, max) for _ in range (size)]

def quicksort(a):
    if len(a)<=1: return a
    minimo,igual,largo=[],[],[]
    pivote=a[randint(0, len(a)-1)]    
    for x in a:
        if x<pivote:    minimo.append(x)
        elif x==pivote: igual.append(x)
        else:           largo.append(x)       
    return quicksort(minimo)+igual+quicksort(largo)

n=[10,100,1000,1000,10000,100000]
times={'quick':[]}
samples=5
for size in n:
    tot_time=0.0
    for _ in range(samples):
        a=crearArreglo(size,size)
        t0=time()
        s=quicksort(a)
        t1=time()
        tot_time+=(t1-t0)
    times['quick'].append(tot_time/float(samples))
    
def Mostrar():        
    cLis.delete(1.0,'end') 
    a=crearArreglo()   
    cLis.insert(1.0, 'Arreglo Desordenado: \n')
    cLis.insert(2.0, a)
    print ("Arreglo Desordenado: ", a)
    s=quicksort(a)
    cLis.insert(3.0, '\n')
    cLis.insert(3.0, s)
    cLis.insert(3.0, 'Arreglo Ordenado: \n')   
    print("Arreglo Ordenado: ",s)
    
def Tiempo():    
    cLis.delete(1.0,'end')        
    print('\nn\t\tQuickSort')
    print(20*'_')
    for i,size in enumerate(n):
        cLis.insert(7.0, '%d\t... %0.5f\n'%(size,times['quick'][i]))
        print ('%d\t... %0.5f'%(size,times['quick'][i]))
    cLis.insert(1.0, '\n')
    cLis.insert(1.0, 20*'_')
    cLis.insert(1.0, 'n\tQuickSort\n')
    cLis.insert(1.0, '\n')
    
frm.pack(fill="both", expand="True")
frm.config(bg="red")
frm.config(width="350", height="480")
frm.config(bd=30)
frm.config(relief="sunken")
frm.config(cursor="pirate")
ListN=[]

Label(frm,text=Ahora.strftime('%d/%m/%Y\n%H:%M:%S')).grid(row=0,column=0)
Label(frm,text='QUICKSORT').grid(row=0,column=1)

BtnIns=Button(frm, text='Tiempo General', command=Tiempo)
BtnIns.grid(row=2,column=2, sticky='s')
BtnIns=Button(frm, text='Arreglo Random', command=Mostrar)
BtnIns.grid(row=2,column=1, sticky='s')

cLis=Text(frm, width=78,height=28)
cLis.grid(row=4,column=0, columnspan=3)
ventana.mainloop()