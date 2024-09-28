# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 20:28:22 2022

@author: LAFB2000
"""

from tkinter import*
from datetime import *

raiz=Tk()
frm=Frame()

raiz.title("Insertar Dato")
raiz.iconbitmap("ufo_IcES.ico")
raiz.geometry("950x680")

frm.pack(fill="both", expand="True")
frm.config(bg="red")
frm.config(width="400", height="330")
frm.config(bd=30)
frm.config(relief="sunken")
frm.config(cursor="pirate")
img1=PhotoImage(file="coplanet.png")
lbl1=Label(frm, image=img1).place(x=350,y=150,width=120, height=120)

AP=StringVar()
AM=StringVar()
N=StringVar()
Lis=list([])



lbl=Label(frm, text="Apellido Paterno:").grid(row=2, column=1, sticky="e", pady="3")
cTxt1=Entry(frm, textvariable=AP).grid(row=2, column=2)   

lbl2=Label(frm, text="Apellido Materno:").grid(row=3,column=1,sticky="e",pady="3")
cTxt2=Entry(frm, textvariable=AM).grid(row=3,column=2)

lbl3=Label(frm, text="Nombre:").grid(row=4,column=1,sticky="e",pady="3")
cTxt3=Entry(frm, textvariable=N).grid(row=4,column=2)

TxtL=Text(frm).grid(row=6, column=1, columnspan=3, sticky="e", pady="3")


def Insertar():
   AP.set(cTxt1())
   Lis.append(self, NT)
   Lis.sort()
   print(NT)
   
   
btnInsert=Button(frm,text="INSERTAR", command=Insertar()).grid(row=5, column=1,sticky="s")



raiz.mainloop()
