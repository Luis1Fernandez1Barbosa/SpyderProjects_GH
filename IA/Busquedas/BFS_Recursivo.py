# -*- coding: utf-8 -*-
"""
Created on Fri May 19 12:05:35 2023

@author: LAFB2000
"""

from collections import deque
 
 
# Una clase para representar un objeto graph
class Graph:
    # Constructor
    def __init__(self, edges, n):
 
        # Una lista de listas para representar una lista de adyacencia
        self.adjList = [[] for _ in range(n)]
 
        # agrega bordes al graph no dirigido
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
 
# Realizar BFS recursivamentemente en el graph
def recursiveBFS(graph, q, discovered):
 
    if not q:
        return
 
    # quitar la queue del nodo frontal e imprimirlo
    v = q.popleft()
    print(v, end=' ')
 
    # do para cada arista (v, u)
    for u in graph.adjList[v]:
        if not discovered[u]:
            # marcarlo como descubierto y ponerlo en queue
            discovered[u] = True
            q.append(u)
 
    recursiveBFS(graph, q, discovered)
 
 
if __name__ == '__main__':
 
    # Lista de bordes de graph según el diagrama anterior
    edges = [
        (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
        (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)
        # vértice 0, 13 y 14 son nodos individuales
    ]
 
    # número total de nodos en el graph (etiquetados de 0 a 14)
    n = 15
 
    # construye un graph a partir de los bordes dados
    graph = Graph(edges, n)
 
    # para realizar un seguimiento de si se descubre un vértice o no
    discovered = [False] * n
 
    # crea una queue para hacer BFS
    q = deque()
 
    # Realizar el recorrido BFS de todos los nodos no descubiertos a
    # cubre todos los componentes conectados de un graph
    for i in range(n):
        if not discovered[i]:
            # marca el vértice de origen como descubierto
            discovered[i] = True
 
            # poner en queue el vértice fuente
            q.append(i)
 
            # inicia el recorrido BFS desde el vértice i
            recursiveBFS(graph, q, discovered)