# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 17:05:35 2022

@author: LAFB2000
"""

def funcionG (a,b,c):
    grande=a
    if b>grande:
        grande=b   
    if c>grande:
        grande=c
    return grande
    
def funcionG2 (a,s):
    grande=a
    for i in a:
        if i==2:
            if(s>grande):
                grande=s
    return grande

def funcionG3 (a,s):
    grande=a
    for i in a:
        if(s>grande):
            grande=s
    return grande

A1=[12,123,432,2,5476,7,3,12,4,6,7]
A2=[3,45,24,67,45,2342]
A3=[12,12323,432]           
print(funcionG(230, 50, 90))
print(funcionG2(A1, A2))
print(funcionG3(A2, A3))
print('**************************************************')


import numpy as np
random_numbers = np.random.randint(low=0, high=6, size=3).tolist()
print(random_numbers)




"""Matrices"""

from tkinter import *
import numpy as np

a=np.array([[0,0,3,0],[0,3,0,0]])
print(a)
b=np.array([[3,2,5,9],[0,2,3,6]])
c=a+b
print(c)
d=np.array([[4,2,3],[0,5,4],[4,6,2],[6,0,2]])
e=np.array([[4,2],[0,4],[4,2],[0,2]])
f=a.dot(e)
print(f)
r=d.transpose()
print(r)
print('**************************************************')

M1 = [[8, 14, -6,0],[12,7,4,0],[-11,3,21,0],[0,0,0,1]]
A1= [[0,4,0,0],[3,0,0,0],[5,0,0,0],[0,0,0,3]]
print(A1)
print(A1[1])
print(A1[0][1])
A3=[]
for row in A1:
    A3.append(row[1])
    print(A3)
print('**************************************************')

for i in A1:    
    print(i)
print('------------------')
for i in M1:
    print([i])    
print('------------------')

"""SUMA DE MATRICES"""
def sumarMat (m1,m2):
    if len(m1)==len(m2) and len(m1[0])==len(m2[0]):
        m3=[]
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m1[0])):
                m3[i].append(0)
        for i in range(len(m3)):
            for j in range (len(m3[0])):
                m3[i][j] = m1[i][j]+m2[i][j]
        return m3
    else:
        return None
print('-------------------------------------------------------------------------')
c=sumarMat(A1, M1)
if c==None:
    print('No se pueden sumar')
else:
    for fila in c:
        print('[', end=' ')
        for elemento in fila:
            print(elemento, end=' ')
        print(']')
        
"""MATRIZ TRANSPUESTA"""
def TransMat (m1):
    m3=[]
    for i in range (len(m1)):
        m3.append([])
        for j in range (len(m1[0])):
            m3[i].append(0)
    for i in range(len(m3)):
        for j in range (len(m3[0])):
          m3[j][i]=m1[i][j]
    return m3
print('-------------------------------------------------------------------------')
c=TransMat(A1)
for fila in c:
    print('[', end=' ')
    for elemento in fila:
        print(elemento, end=' ')
    print(']')
print(A1)

"""MATRIZ DISPERSA"""
def MatDisp (m1):
    m2=[]
    for i in range (len(m1)):
        for j in range(len(m1[0])):
            if m1[i][j]!=0:
                m2[i][j].append(0)
                return m2
            else:
                return None            
print('-------------------------------------------------------------------------')

for i in A1:
    print('[', end=' ')
    for j in i:
        print(j, end=' ')
    print(']')
print(A1)        

"""RELLENAR MATRIZ"""
def RellMat(m1):
    filas=int(input("Filas:"))
    columnas=int(input("Col:"))
    m1=[]
    for i in range(filas):
        m1.append([])
        for j in range(columnas):
            valor=float(input("Fila{}, Col{}: ".format(i+1, j+1)))
            m1[i].append(valor)
    for fila in m1:
        print('[')
        for elemento in fila:
            print('{:5.1f}'.format(elemento, end=' '))
        print(']')
print('-------------------------------------------------------------------------')


"""ColaCircular"""
# Python3 program for insertion and 
# deletion in Circular Queue 
# Structure of a Node 
class Node:
    def __init__(self):
        self.data = None
        self.link = None
  
class Queue:
    def __init__(self):
        front = None
        rear = None
  
# Function to create Circular queue 
def enQueue(q, value):
    temp = Node() 
    temp.data = value 
    if (q.front == None): 
        q.front = temp 
    else:
        q.rear.link = temp 
  
    q.rear = temp 
    q.rear.link = q.front
  
# Function to delete element from 
# Circular Queue 
def deQueue(q):
    if (q.front == None):
        print("Queue is empty") 
        return -999999999999
  
    # If this is the last node to be deleted 
    value = None # Value to be dequeued 
    if (q.front == q.rear):
        value = q.front.data
        q.front = None
        q.rear = None
    else: # There are more than one nodes 
        temp = q.front 
        value = temp.data 
        q.front = q.front.link 
        q.rear.link = q.front
  
    return value 
  
# Function displaying the elements 
# of Circular Queue 
def displayQueue(q):
    temp = q.front 
    print("Elements in Circular Queue are: ", 
                                   end = " ") 
    while (temp.link != q.front):
        print(temp.data, end = " ") 
        temp = temp.link
    print(temp.data)
  
# Driver Code
if __name__ == '__main__':
  
    # Create a queue and initialize
    # front and rear 
    q = Queue() 
    q.front = q.rear = None
  
    # Inserting elements in Circular Queue 
    enQueue(q, 14) 
    enQueue(q, 22) 
    enQueue(q, 6) 
    enQueue(q, 8)
    enQueue(q, 9)
    enQueue(q, 0)
    enQueue(q, 120030) 
  
    # Display elements present in 
    # Circular Queue 
    displayQueue(q) 
  
    # Deleting elements from Circular Queue 
    print("Deleted value = ", deQueue(q)) 
    print("Deleted value = ", deQueue(q)) 
  
    # Remaining elements in Circular Queue 
    displayQueue(q) 
  
    enQueue(q, 9) 
    enQueue(q, 20) 
    displayQueue(q)
  
# This code is contributed by PranchalK




