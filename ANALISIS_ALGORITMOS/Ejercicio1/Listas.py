# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 22:38:28 2022

@author: LAFB2000
"""

if __name__=="__main__":
    nombres=["Juan","Rosa","Rebeca"]
    edad=[34,10,'23']
    Personas=[]
    
   
    print(nombres)
    print(edad)
  
    for i in nombres:
        print(i)
    for i in edad:
        print(i*2)
    for i in nombres:
        print(len(i))
    
    nombres.append('Mz324235')
    print(nombres)
    
    nombres.sort()
    print(nombres)
    
A1= [[0,4,0,0],[3,0,0,0],[5,0,0,0],[0,0,0,3]]
print(A1)