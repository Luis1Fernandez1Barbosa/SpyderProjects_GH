# -*- coding: utf-8 -*-
"""
Created on Sat May  7 11:25:27 2022

@author: LAFB2000
"""

from Nodo import Nodo

class PilaLig():
    
    def __init__(self):
        self.primero=None
        self.ultimo=None
        
    def Vacia(self):
        return self.primero == None
       
    def AgregIni(self,dato):
        if self.Vacia():
            self.primero=self.ultimo=Nodo(dato)
            self.ultimo.siguiente=self.primero
        else:
            temp=Nodo(dato)
            temp.siguiente = self.primero
            self.primero=temp
            self.ultimo.siguiente = self.primero
    
    def RemFin(self):
        if self.Vacia():
            print('Lista Vacia')
        elif self.primero == self.ultimo:
            self.primero = self.ultimo =None
        else:
            temp =self.primero
            while temp.siguiente != self.ultimo:
                temp =temp.siguiente
            temp.siguiente=self.primero
            self.ultimo =temp
            
    def Recorrer(self):
        temp= self.primero
        while temp.siguiente != self.primero:
            print(temp.dato)
            temp=temp.siguiente
        print(temp.dato)