# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 07:26:05 2022

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
ventana.geometry("600x480")

B01=np.array([[1,2],[3,4],[5,6]])
B0=np.array([[1,2,3],[4,5,6]])
B1=np.array([[2,4,5,7,0,1],[1,9,0,5,6,8],[4,2,5,9,0,2],[3,4,5,6,7,8]])
B2=np.array([[45,76,23,98,12],[15,23,44,76,94],[41,21,51,81,11]])
B3=np.array([[137,234,543],[776,987,654],[410,910,453],[304,704,900],[200,500,330]])
B4=np.array([[7000,1765,1223,4324],[9000,3543,3455,3245],[4520,5565,6344,5634],[5430,6540,5076,6086],[8607,7686,1546,3212],[2040,4034,3402,2130],[4534,5390,7650,7680],[4605,5605,9800,7098]])

"""------------------------------------------"""
 

def transpuesta_1(Matriz1):
    print("Matriz Incial:")
    print(Matriz1)
    MatrizA=[[Matriz1 [j][i] for j in range(len(Matriz1))] for i in range(len(Matriz1[0]))]
    print("Matriz Transpuesta:")
    print(MatrizA)
    cLis.insert(1.0,'\n')
    cLis.insert(2.0, MatrizA) 
    cLis.insert(1.0, "Matriz Transpuesta: ")
    cLis.insert(1.0,'\n')
    cLis.insert(1.0,'\n')
    z=multiMat(Matriz1, MatrizA)
    impri(z)  
    #cLis.insert(1.0,'\n')
    cLis.insert(1.0, 'Matriz Final: (multiplicacion de matrices)')

def multiMat(m1,m2):
    if len(m1[0])==len(m2):
        m3=[]
        for i in range (len(m1)):
           m3.append([])
           for j in range (len(m2[0])):
                  m3[i].append(0)
                  
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m1[0])):
                    m3[i][j] += m1[i][k] * m2[k][j]
        return m3
    else:
        return None

def impri(c):
    if c==None:
        cLis.insert(1.0,'No se pueden sumar')
    else:
        cLis.insert(2.0,']')
        for fila in c:
            cLis.insert(2.0,']')        
            for elemento in fila:         
                cLis.insert(2.0, '  ')
                cLis.insert(2.0, elemento)               
            cLis.insert(2.0,'[')      
    cLis.insert(2.0,'[')

"""-----------------------------------------"""
def InsertarMatrA1 ():
    print(B1) 
    cLis.delete(1.0,"end")
    cLis.insert(1.0,'\n')
    cLis.insert(2.0, B1)
    cLis.insert(1.0, "Matriz B1: ")
    cLis.insert(1.0,'\n')
    MatrizA=transpuesta_1(B1)
    z=multiMat(B1, MatrizA)
    impri(z)  
def InsertarMatrA2 ():
    print(B2)
    cLis.delete(1.0,"end")
    cLis.insert(1.0,'\n')
    cLis.insert(2.0, B2)
    cLis.insert(1.0, "Matriz B2: ")
    cLis.insert(1.0,'\n')
    transpuesta_1(B2)
def InsertarMatrA3 ():
    print(B3)
    cLis.delete(1.0,"end")
    cLis.insert(1.0,'\n')
    cLis.insert(2.0, B3)
    cLis.insert(1.0,"Matriz B3: ")
    cLis.insert(1.0,'\n')
    transpuesta_1(B3)
def InsertarMatrA4 ():
    print(B4)
    cLis.delete(1.0,"end")
    cLis.insert(1.0,'\n')
    cLis.insert(1.0, B4)
    cLis.insert(1.0,'\n')
    cLis.insert(1.0, "Matriz B4: ")
    cLis.insert(1.0,'\n')
    transpuesta_1(B4)
"""------------------------------"""

frm.pack(fill="both", expand="True")
frm.config(bg="red")
frm.config(width="350", height="480")
frm.config(bd=30)
frm.config(relief="sunken")
frm.config(cursor="pirate")

Label(frm,text=Ahora.strftime('%d/%m/%Y\n%H:%M:%S')).grid(row=0,column=0)
Label(frm,text="DOS MATRICES").grid(row=0,column=1)
Label(frm, text="Elija matriz:").grid(row=0, column=2, sticky="e", pady="3")

BtnIns=Button(frm, text='Matriz B1', command=InsertarMatrA1)
BtnIns.grid(row=2,column=2, sticky='n')
BtnIns=Button(frm, text='Matriz B2', command=InsertarMatrA2)
BtnIns.grid(row=3,column=2, sticky='n')
BtnIns=Button(frm, text='Matriz B3', command=InsertarMatrA3)
BtnIns.grid(row=4,column=2, sticky='n')
BtnIns=Button(frm, text='Matriz B4', command=InsertarMatrA4)
BtnIns.grid(row=5,column=2, sticky='n')

cLis=Text(frm, width=60,height=22)
cLis.grid(row=2,column=0, columnspan=2, rowspan=7)
ventana.mainloop()