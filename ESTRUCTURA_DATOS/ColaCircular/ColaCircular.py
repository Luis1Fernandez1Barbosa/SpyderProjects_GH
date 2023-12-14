# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 20:18:01 2022

@author: LAFB2000
"""
from Nodo import Nodo
from tkinter import *

class ColaCir():
    
    def __init__(self):
        self.primero=None
        self.ultimo=None
        
    def Vacia(self):
        return self.primero == None
       
    def AgregFin(self,dato):
        if self.Vacia():
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.siguiente = self.primero
        else:
            temp = self.ultimo
            self.ultimo =temp.siguiente =Nodo(dato)
            self.ultimo.siguiente = self.primero
            
    def RemIni(self):
        if self.Vacia():
            print('lista vacia')
        elif self.primero ==self.ultimo:
            self.primero=self.ultimo =None
        else:
            self.primero =self.primero.siguiente
            self.ultimo.siguiente = self.primero
            
    def Recorrer(self):
        temp= self.primero
        while temp.siguiente != self.primero:
            print(temp.dato)           
            temp=temp.siguiente
        print(temp.dato)
        print('-----------------Vuelta (Reinicio)')
        temp= self.primero
        while temp.siguiente != self.primero:
            print(temp.dato)
            temp=temp.siguiente
        print(temp.dato)
