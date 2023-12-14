# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 00:50:27 2022

@author: LAFB2000
"""

from tkinter import *
import datetime

Ahora=datetime.datetime.now()
print(Ahora.strftime('%d/%m/%Y\n%H:%M:%S'))

ventana=Tk()
frm=Frame()
ventana.title("COLA DE DOBLE ENTRADA")
ventana.geometry("350x480")

def InsetarIni ():
    i=Entra.get()
    if (i=='' or i==' ' or i=='  ' or i=='   '):
        ventana=Tk()
        ventana.title("¡¡¡ERROR!!!")
        ventana.geometry("300x100")    
        Label(ventana, text='¡¡INSERTE UN DATO!!').pack()
        return Entra.set('')
    else:
        ListN.insert(0,i)
        cLis.insert(1.0, "\n")
        for i in ListN:
            print (ListN)
            cLis.insert(1.0,ListN)
            return Entra.set('')

def InsetarFin ():
    i=Entra.get()
    if (i=='' or i==' ' or i=='  ' or i=='   '):
        ventana=Tk()
        ventana.title("¡¡¡ERROR!!!")
        ventana.geometry("300x100")    
        Label(ventana, text='¡¡INSERTE UN DATO!!').pack()
        return Entra.set('')
    else:
        ListN.append(i)
        cLis.insert(1.0, "\n")
        for i in ListN:
            print (ListN)
            cLis.insert(1.0,ListN)
            return Entra.set('')
        
def VaciarIni():
    cLis.delete(1.0, "end")
    cLis.insert(1.0, ListN)
    cLis.insert(2.0, "\n")
    V=ListN.pop(0)
    print(ListN)
    print('Elemento fuera: ' + V)
    cLis.insert(3.0, ListN)
    cLis.insert(4.0, "\nElemento fuera: " + V)
    cLis.insert(2.0, '-----------------------------------')

def VaciarFin():
    cLis.delete(1.0, "end")
    cLis.insert(1.0, ListN)
    cLis.insert(2.0, "\n")
    V=ListN.pop()
    print(ListN)
    print('Elemento fuera: ' + V)
    cLis.insert(3.0, ListN)
    cLis.insert(4.0, "\nElemento fuera: " + V)
    cLis.insert(2.0, '-----------------------------------')
    
frm.pack(fill="both", expand="True")
frm.config(bg="red")
frm.config(width="350", height="480")
frm.config(bd=30)
frm.config(relief="sunken")
frm.config(cursor="pirate")
ListN=[]

Label(frm,text=Ahora.strftime('%d/%m/%Y\n%H:%M:%S')).grid(row=0,column=0)
Label(frm,text='COLA DE DATOS').grid(row=0,column=1)
Label(frm, text="Inserte dato en cola: ").grid(row=1, column=0, sticky="e", pady="3")

Entra=StringVar() 
ctxt=Entry(frm, textvariable=Entra).grid(row=1,column=1)

BtnIns=Button(frm, text='Insertar inicio', command=InsetarIni)
BtnIns.grid(row=2,column=0, sticky='s')
BtnIns=Button(frm, text='Insertar fin', command=InsetarFin)
BtnIns.grid(row=2,column=1, sticky='s')
BtnIns=Button(frm, text='Extraer inicio', command=VaciarIni)
BtnIns.grid(row=3,column=0, sticky='s')
BtnIns=Button(frm, text='Extraer final', command=VaciarFin)
BtnIns.grid(row=3,column=1, sticky='s')

cLis=Text(frm, width=35,height=20)
cLis.grid(row=4,column=0, columnspan=3)
ventana.mainloop()