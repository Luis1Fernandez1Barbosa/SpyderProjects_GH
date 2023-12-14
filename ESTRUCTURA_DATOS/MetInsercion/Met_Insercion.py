# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 19:17:32 2022

@author: LAFB2000
"""
from tkinter import *
import datetime

Ahora=datetime.datetime.now()
print(Ahora.strftime('%d/%m/%Y\n%H:%M:%S'))

ventana=Tk()
frm=Frame()
ventana.title("METODO DE ORDENAMIENTO")
ventana.geometry("450x480")

def InsetarD ():
    i=Entra.get()
    if (i=='' or i==' ' or i=='  ' or i=='   '):
        ventana=Tk()
        ventana.title("¡¡¡ERROR!!!")
        ventana.geometry("300x200")    
        Label(ventana, text='¡¡INSERTE UN DATO!!').pack()
        return Entra.set('')
    else:
        ListN.append(int(i))
        cLis.insert(1.0, "\n")
        for i in ListN:
            print (ListN)
            cLis.insert(1.0,ListN)
            return Entra.set('')
"""----------------------------------------------"""

def metInser():
    cLis.delete(1.0,'end')
    print('Arreglo: ', ListN)
    cLis.insert(1.0,'\n')
    cLis.insert(1.0,ListN)
    cLis.insert(1.0, "Arreglo Inicial: ")
    for i in range (1,len(ListN)):
        tar=ListN[i]
        ind=i-1
        while(ind>=0 and ListN[ind]>tar):
            ListN[ind+1] = ListN[ind]
            ind-=1
        ListN[ind+1]=tar
    print('Arreglo final: ', ListN)
    cLis.insert(2.0,ListN)
    cLis.insert(2.0, "Arreglo Ordenado: ")

"""-----------------------------------------------"""
frm.pack(fill="both", expand="True")
frm.config(bg="red")
frm.config(width="350", height="480")
frm.config(bd=30)
frm.config(relief="sunken")
frm.config(cursor="pirate")
ListN=[]

Label(frm,text=Ahora.strftime('%d/%m/%Y\n%H:%M:%S')).grid(row=0,column=0)
Label(frm,text='MÉTODO DE INSERCIÓN').grid(row=0,column=1)
Label(frm, text="Escriba el número: ").grid(row=1, column=0, sticky="e", pady="3")

Entra=StringVar() 
ctxt=Entry(frm, textvariable=Entra).grid(row=1,column=1)

BtnIns=Button(frm, text='Insertar Dato', command=InsetarD)
BtnIns.grid(row=2,column=1, sticky='s')
BtnIns=Button(frm, text='Ordenar', command=metInser)
BtnIns.grid(row=2,column=2, sticky='s')

cLis=Text(frm, width=48,height=20)
cLis.grid(row=3,column=0, columnspan=3)
ventana.mainloop()