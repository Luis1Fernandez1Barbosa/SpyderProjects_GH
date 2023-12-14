# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 12:35:25 2022

@author: LAFB2000
"""
def funcionUno(a):
    print(a*2)
def funcionDos(a):
    return len(a)


if __name__=="__main__":
    cadena="México siempre fiel"
    print(cadena)
    
    #recorrer cadena
    print(cadena[0:6]) 
    """n-1_[0:6]=5"""
    print(cadena[7:])
    """de n-1 al final"""
    print(cadena[:8])
    """de inicio a n-1"""
    print(cadena[:-4])
    """del final a la posición n de derecha a izquierda"""
    print(cadena[-4:])
    
    print(len(cadena))
    print(cadena.split())
    print(cadena.split("e"))
    
    print(cadena*3)
    
    ncadena="m"+cadena[1:]
    print(ncadena)
    
    print(cadena.replace("M", "m"))
    
    cadena.replace("M", "m")
    print(cadena)
    
    n1cadena=cadena.replace("M", "m")
    print(n1cadena)
    
    
    if("fiel" in cadena):
        print("Si esta")
    else:
        print("No esta")
    if(len(cadena)>7):
        print("mayor o igual a 7")
    funcionUno(cadena)
    funcionUno(23)
    
    print(funcionDos("sapos"))
    