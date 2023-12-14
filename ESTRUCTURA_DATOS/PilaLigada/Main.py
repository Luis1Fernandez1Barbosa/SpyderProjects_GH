# -*- coding: utf-8 -*-
"""
Created on Sat May  7 11:25:27 2022

@author: LAFB2000
"""
from PilaLigada import PilaLig
from tkinter import *
import datetime

ListA = PilaLig()
Ahora=datetime.datetime.now()
print(Ahora.strftime('%d/%m/%Y\n%H:%M:%S'))

ventana=Tk()
frm=Frame()
ventana.title("Listas Enlazadas")
ventana.geometry("320x380")

"""----------------------------------------------------------------"""
def InsertarIni ():
    i=Entra.get()
    if (i=='' or i==' ' or i=='  ' or i=='   '):
        ventana=Tk()
        ventana.title("¡¡¡ERROR!!!")
        ventana.geometry("300x100")    
        Label(ventana, text='¡¡INSERTE UN DATO!!').pack()
        return Entra.set('')
    else:
        ListA.AgregIni(int(i))
        cLis.insert(1.0, "\n")
        cLis.insert(1.0,i)
        return Entra.set('')    
        cLis.insert(2.0, '---------------------')
"""----------------------------------------------------------------"""
def Remover():
    ListA.RemFin()
    cLis.insert(1.0,'elemento eliminado\n')
 
def Recor():
    ListA.Recorrer()
    cLis.delete(1.0,'end')
    cLis.insert(1.0,'Lista Recorrida')
    print('-----------------------')
  

frm.pack(fill="both", expand="True")
frm.config(bg="red")
frm.config(width="450", height="580")
frm.config(bd=30)
frm.config(relief="sunken")
frm.config(cursor="pirate")

Label(frm,text=Ahora.strftime('%d/%m/%Y\n%H:%M:%S')).grid(row=0,column=0)
Label(frm,text='PILA LIGADA').grid(row=0,column=1)
Label(frm, text="Inserte dato:  ").grid(row=1, column=0, sticky="e", pady="3")

Entra=StringVar() 
ctxt=Entry(frm, textvariable=Entra).grid(row=1,column=1)

BtnIns=Button(frm, text='Insertar Dato', command=InsertarIni)
BtnIns.grid(row=2,column=1, sticky='s')
BtnIns=Button(frm, text='Sacar Dato', command=Remover)
BtnIns.grid(row=2,column=2, sticky='s')
BtnIns=Button(frm, text='Recorrer', command=Recor)
BtnIns.grid(row=2,column=0, sticky='s')

cLis=Text(frm, width=25,height=15)
cLis.grid(row=3,column=0, columnspan=3)
ventana.mainloop()