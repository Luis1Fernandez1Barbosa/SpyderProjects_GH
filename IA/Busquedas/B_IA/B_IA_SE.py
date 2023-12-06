# -*- coding: utf-8 -*-
"""
Created on Sat May 27 19:45:48 2023

@author: LAFB2000
"""
"""
FERNÁNDEZ BARBOSA LUIS ANTONIO
IA 2909
SE 2007
"""
import pprint
import os
import time
dir(os)
# Pprint para mostrar el grafo de manera leible
pp = pprint.PrettyPrinter(indent=4)
# Grafo principal
grafo_principal = {}

# Carga el grafo_principal a traves del .txt
with open('grafo_p.txt', 'r') as f:
    for l in f:
        nodo_a, nodo_b, coste = l.split()
        if nodo_a not in grafo_principal:
            grafo_principal[nodo_a] = {}
        grafo_principal[nodo_a][nodo_b] = int(coste)
        if nodo_b not in grafo_principal:
            grafo_principal[nodo_b] = {}
        grafo_principal[nodo_b][nodo_a] = int(coste)

# Busqueda en Amplitud (Breadth First Search - BFS)
def B_Amplitud_SH(grafo, inicio, destino):
    cola = [(inicio, [inicio], 0)]
    visitado = {inicio}
    while cola:
        (node, ruta, coste) = cola.pop(0)
        for temp in grafo[node].keys():
            if temp == destino:
                return ruta + [temp], coste + grafo[node][temp]
            else:
                if temp not in visitado:
                    visitado.add(temp)
                    cola.append((temp, ruta + [temp], coste + grafo[node][temp]))
                    
# Busqueda en Amplitud sentido antihorario(Breadth First Search - BFS)
def B_Amplitud_SAH(grafo, inicio, destino):
    cola = [(inicio, [inicio], 0)]
    visitado = {inicio}
    while cola:
        (node, ruta, coste) = cola.pop()
        for temp in grafo[node].keys():
            if temp == destino:
                return ruta + [temp], coste + grafo[node][temp]
            else:
                if temp not in visitado:
                    visitado.add(temp)
                    cola.append((temp, ruta + [temp], coste + grafo[node][temp]))


# Busqueda en Profundidad (Depth First Search Method - DFS)
def B_Profundidad_SH(grafo, inicio, destino):
    pila = [(inicio, [inicio], 0)]
    visitado = {inicio}
    while pila:
        (node, ruta, coste) = pila.pop()
        for temp in grafo[node].keys():
            if temp == destino:
                return ruta + [temp], coste + grafo[node][temp]
            else:
                if temp not in visitado:
                    visitado.add(temp)
                    pila.append((temp, ruta + [temp], coste + grafo[node][temp]))

# Busqueda en Profundidad sentido antihorario (Depth First Search Method - DFS)
def B_Profundidad_SAH(grafo, inicio, destino):
    pila = [(inicio, [inicio], 0)]
    visitado = {inicio}
    while pila:
        (node, ruta, coste) = pila.pop(0)
        for temp in grafo[node].keys():
            if temp == destino:
                return ruta + [temp], coste + grafo[node][temp]
            else:
                if temp not in visitado:
                    visitado.add(temp)
                    pila.append((temp, ruta + [temp], coste + grafo[node][temp]))


# Iterative Deepening Search Method (Busqueda en Profundidad Iterativa)
def BP_Itera(grafo, inicio, destino):
    nivel = 0
    contador = 0
    pila = [(inicio, [inicio], 0)]
    visitado = {inicio}
    while True:
        nivel += 1
        while pila:
            if contador <= nivel:
                contador = 0
                (node, ruta, coste) = pila.pop()
                for temp in grafo[node].keys():
                    if temp == destino:
                        return ruta + [temp], coste + grafo[node][temp]
                    else:
                        if temp not in visitado:
                            visitado.add(temp)
                            contador += 1
                            pila.append((temp, ruta + [temp], coste + grafo[node][temp]))
            else:
                q = pila
                visitado_bfs = {inicio}
                while q:
                    (node, ruta, coste) = q.pop(0)
                    for temp in grafo[node].keys():
                        if temp == destino:
                            return ruta + [temp], coste + grafo[node][temp]
                        else:
                            if temp not in visitado_bfs:
                                visitado_bfs.add(temp)
                                q.append((temp, ruta + [temp], coste + grafo[node][temp]))
                break


# Busqueda Escalada Simple
def B_Escalada(grafo, inicio, destino):
      # crear ruta inicial aleatoria
      pila = [(inicio, [inicio], 0)]
      visitado = {inicio}
      while pila:
          (node, ruta, coste) = pila.pop(0)
          #ruta=[]
          for temp in grafo[node].keys():
             if temp == destino:
                 coste_n=coste + grafo[node][temp]
                 return ruta + [temp], coste_n
                 #random.shuffle(ruta)
             else:
                #for cost in grafo[coste].keys():
                    #if cost <= cost.next:
                if temp not in visitado:
                    visitado.add(temp)
                    coste_n=coste + grafo[node][temp]
                    pila.append((temp, ruta + [temp], coste_n))    
            

n = 1
while n == 1:
    os.system("CLS")
    print("""============================================
                Grafo Completo
============================================""")
    pp.pprint(grafo_principal)
    print("""============================================
[1] Amplitud sentido horario
[2] Amplitud sentido antihorario
[3] Profundidad sentido horario
[4] Profundidad sentido antihorario
[5] Profundidad Iterativa
[6] Escalada simple
[0] Salir
============================================""")
    x = input("Opcion: ")
    if x == '1':
        inicio = input("Ingresa el Inicio: ")
        while inicio not in grafo_principal:
            print("Nodo no encontrado intenta nuevamente")
            inicio = input("Ingresa el Inicio: ")
        destino = input("Ingresa el Destino: ")
        while destino not in grafo_principal:
            print("Nodo no encontrado intenta nuevamente")
            destino = input("Ingresa el Destino: ")
        print("""============================================
                 Ruta
============================================""")
        print (B_Amplitud_SH(grafo_principal, inicio, destino))
        print("============================================\nEspere 10 segundos ...")
        os.system("pause")
        time.sleep(10)

    elif x == '2':
        inicio = input("Ingresa el Inicio: ")
        while inicio not in grafo_principal:
            print("Nodo no encontrado intenta nuevamente")
            inicio = input("Ingresa el Inicio: ")
        destino = input("Ingresa el Destino: ")
        while destino not in grafo_principal:
            print("Nodo no encontrado intenta nuevamente")
            destino = input("Ingresa el Destino: ")
        print("""============================================
              Ruta seguida:
============================================""")
        print (B_Amplitud_SAH(grafo_principal, inicio, destino))
        print("============================================\nEspere 10 segundos ...")
        os.system("pause")
        time.sleep(10)

    elif x == '3':
        inicio = input("Ingresa el Inicio: ")
        while inicio not in grafo_principal:
            print("Nodo no encontrado intenta nuevamente")
            inicio = input("Ingresa el Inicio: ")
        destino = input("Ingresa el Destino: ")
        while destino not in grafo_principal:
            print("Nodo no encontrado intenta nuevamente")
            destino = input("Ingresa el Destino: ")
        print("""============================================
                 Ruta seguida:
============================================""")
        print (B_Profundidad_SH(grafo_principal, inicio, destino))
        print("============================================\nEspere 10 segundos ...")
        os.system("pause")
        time.sleep(10)

    elif x == '4':
        inicio = input("Ingresa el Inicio: ")
        while inicio not in grafo_principal:
            print("Nodo no encontrado intenta nuevamente")
            inicio = input("Ingresa el Inicio: ")
        destino = input("Ingresa el Destino: ")
        while destino not in grafo_principal:
            print("Nodo no encontrado intenta nuevamente")
            destino = input("Ingresa el Destino: ")
        print("""============================================
                 Ruta seguida:
============================================""")
        print (B_Profundidad_SAH(grafo_principal, inicio, destino))
        print("============================================\nEspere 10 segundos ...")
        os.system("pause") 
        time.sleep(10)

    elif x == '5':
        inicio = input("Ingresa el Inicio: ")
        while inicio not in grafo_principal:
            print("Nodo no encontrado intenta nuevamente")
            inicio = input("Ingresa el Inicio: ")
        destino = input("Ingresa el Destino: ")
        while destino not in grafo_principal:
            print("Nodo no encontrado intenta nuevamente")
            destino = input("Ingresa el Destino: ")
        print("""============================================
                 Ruta seguida:
============================================""")
        print (BP_Itera(grafo_principal, inicio, destino))
        print("============================================\nEspere 10 segundos ...")
        os.system("pause")
        time.sleep(10)
    
    elif x == '6':
        inicio = input("Ingresa el Inicio: ")
        while inicio not in grafo_principal:
            print("Nodo no encontrado intenta nuevamente")
            inicio = input("Ingresa el Inicio: ")
        destino = input("Ingresa el Destino: ")
        while destino not in grafo_principal:
            print("Nodo no encontrado intenta nuevamente")
            destino = input("Ingresa el Destino: ")
        print("""============================================
              Ruta seguida:
============================================""")
        print (B_Escalada(grafo_principal,inicio,destino))
        print("============================================\nEspere 10 segundos ...")
        os.system("pause")
        time.sleep(10)
    
    
    elif x=='0':
        print("Saliendo del programa...")
        time.sleep(3)
        exit()
