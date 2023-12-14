# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 01:16:30 2022

@author: LAFB2000
"""
from tkinter import *

ventana=Tk()
frm=Frame()
ventana.title("INSERTAR UN DATO")
ventana.geometry("350x480")

def InsetarD ():
    i=Entra.get()
    if (i=='' or i==' ' or i=='  ' or i=='   '):
        ventana=Tk()
        ventana.title("¡¡¡ERROR!!!")
        ventana.geometry("300x100")    
        Label(ventana, text='¡¡INSERTE UN DATO!!').pack()
        return Entra.set('')
    else:
        ListN.append(i)
        for i in ListN:
            print (ListN)
            cLis.insert(1.0,ListN)
            return Entra.set('')
        
def Ordenar():
    cLis.delete(1.0, "end")
    ListN.sort()
    print(ListN)
    for i in ListN:
        if (i=='    ' or i== '     '):
            ListN.remove(i)
            print(ListN)
    cLis.insert(1.0, ListN)

frm.pack(fill="both", expand="True")
frm.config(bg="red")
frm.config(width="350", height="480")
frm.config(bd=30)
frm.config(relief="sunken")
frm.config(cursor="pirate")
ListN=[]

Label(frm,text='LISTA DE NOMBRES').grid(row=0,column=1)
Label(frm, text="Nombre\no\nApellido:").grid(row=1, column=0, sticky="e", pady="3")

Entra=StringVar() 
ctxt=Entry(frm, textvariable=Entra).grid(row=1,column=1)

BtnIns=Button(frm, text='Insertar Dato', command=InsetarD)
BtnIns.grid(row=2,column=1, sticky='s')
BtnIns=Button(frm, text='Ordenar', command=Ordenar)
BtnIns.grid(row=2,column=2, sticky='s')

cLis=Text(frm, width=35,height=20)
cLis.grid(row=3,column=0, columnspan=3)
ventana.mainloop()