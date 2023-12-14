# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 01:15:48 2022

@author: LAFB2000
"""
from tkinter import *
import datetime
import numpy as np

Ahora=datetime.datetime.now()
print(Ahora.strftime('%d/%m/%Y\n%H:%M:%S'))

ventana=Tk()
frm=Frame()
ventana.title("MATRICES")
ventana.geometry("570x400")

A1=np.array([[0,0,0,0,0,2,2,0,0,1],[1,0,0,9,0,0,0,0,0,1],[0,0,4,0,0,0,0,0,5,0]])
A2=np.array([[0,0,0,0,0,0,0,0],[1,0,0,0,9,0,0,0],[4,0,2,5,0,8,0,1]])
A3=np.array([[0,0,0,13,0,0,0,0,7,0],[0,0,0,0,0,11,0,0,0,0],[41,0,0,0,0,0,9,0,1,0],[0,0,3,0,0,0,7,0,0,0],[0,0,0,0,0,0,0,0,0,0]])
A4=np.array([[0,1,0,0],[9,0,0,0],[4,0,5,6],[0,0,0,0],[0,0,1,3],[200,0,0,0],[0,90,0,0],[0,0,0,0]])
A5=np.array([[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,5],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,5000,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3800,0,0,0]])
A6=np.array([[16, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 5], [0, 0, 4, 0]])
"""-----------------------------------------"""
def MatDisp(Matriz1):
    print("Matriz Incial:")
    print(Matriz1)
    MatrizDisp = []
    rows, cols = Matriz1.shape
    for i in range(rows):
        for j in range(cols):
            if Matriz1[i][j] != 0:
                triplet = [i+1, j+1, Matriz1[i][j]]
                MatrizDisp.append(triplet)
    print("Matriz Compacta:")
    print(MatrizDisp)
    cLis.insert(1.0,'\n')
    cLis.insert(1.0, MatrizDisp)
    cLis.insert(2.0,'\n')
    cLis.insert(1.0, "Matriz Compacta: ")
"""-----------------------------------------"""
def InsertarMatrA1 ():
    print(A1) 
    cLis.delete(1.0,"end")
    cLis.insert(1.0,'\n')
    cLis.insert(2.0, A1)
    cLis.insert(1.0, "Matriz Dispersa: ")
    MatDisp(A1)
def InsertarMatrA2 ():
    print(A2)
    cLis.delete(1.0,"end")
    cLis.insert(1.0,'\n')
    cLis.insert(2.0, A2)
    cLis.insert(1.0, "Matriz Dispersa: ")
    MatDisp(A2)
def InsertarMatrA3 ():
    print(A3)
    cLis.delete(1.0,"end")
    cLis.insert(1.0,'\n')
    cLis.insert(2.0, A3)
    cLis.insert(1.0,"Matriz Dispersa: ")
    MatDisp(A3)
def InsertarMatrA4 ():
    print(A4)
    cLis.delete(1.0,"end")
    cLis.insert(1.0,'\n')
    cLis.insert(1.0, A4)
    cLis.insert(1.0,'\n')
    cLis.insert(1.0, "Matriz Dispersa: ")
    MatDisp(A4)
def InsertarMatrA5 ():  
    print(A5)
    cLis.delete(1.0,"end")
    cLis.insert(1.0,'\n')
    cLis.insert(2.0, A5)
    cLis.insert(1.0, "Matriz Dispersa: ")
    MatDisp(A5)
def InsertarMatrA6 ():
    print(A6)
    cLis.delete(1.0,"end")
    cLis.insert(1.0,'\n')
    cLis.insert(2.0, A6)
    cLis.insert(1.0, "Matriz Dispersa: ")
    MatDisp(A6)
"""----------------------------------------------"""

"""-----------------------------------------------"""
frm.pack(fill="both", expand="True")
frm.config(bg="red")
frm.config(width="350", height="480")
frm.config(bd=30)
frm.config(relief="sunken")
frm.config(cursor="pirate")

Label(frm,text=Ahora.strftime('%d/%m/%Y\n%H:%M:%S')).grid(row=0,column=0)
Label(frm,text='MATRIZ COMPACTA').grid(row=0,column=1)
Label(frm, text="Elija matriz:").grid(row=0, column=2, sticky="e", pady="3")

BtnIns=Button(frm, text='Matriz A1', command=InsertarMatrA1)
BtnIns.grid(row=2,column=2, sticky='n')
BtnIns=Button(frm, text='Matriz A2', command=InsertarMatrA2)
BtnIns.grid(row=3,column=2, sticky='n')
BtnIns=Button(frm, text='Matriz A3', command=InsertarMatrA3)
BtnIns.grid(row=4,column=2, sticky='n')
BtnIns=Button(frm, text='Matriz A4', command=InsertarMatrA4)
BtnIns.grid(row=5,column=2, sticky='n')
BtnIns=Button(frm, text='Matriz A5', command=InsertarMatrA5)
BtnIns.grid(row=6,column=2, sticky='n')
BtnIns=Button(frm, text='Matriz A6', command=InsertarMatrA6)
BtnIns.grid(row=7,column=2, sticky='n')

cLis=Text(frm, width=57,height=18)
cLis.grid(row=2,column=0, columnspan=2, rowspan=7)
ventana.mainloop()