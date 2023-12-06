# -*- coding: utf-8 -*-
"""
Created on Sun May 21 21:26:20 2023

@author: LAFB2000
"""
import numpy as np

import matplotlib
matplotlib.__version__
import matplotlib.pyplot as plt


edad_x=[20,25,30,35,40,45,50,55,60,65]
salario_a_y=[201,202, 203,204,205,206,207,208,209,210]
salario_b_y=[100,101,102,104,105,106,107,108,109,110]
salario_c_y=[10,9,8,7,6,5,4,3,2,1]


plt.style.use('default')
width=0.1

edad_np_x=np.arange(len(edad_x))
plt.barh(edad_np_x-2*width,salario_a_y, label="profesión a")
#,width=width)
plt.barh(edad_np_x,salario_b_y,label="profesion b")
#,width=width)

plt.barh(edad_np_x+2*width,salario_c_y,label="profesion c")
#width=width)
salario_medio=np.sum([salario_a_y,salario_b_y,salario_c_y],axis=0)/3
plt.barh(edad_np_x+4*width,salario_medio,label="salario_medio",color="black")
#,width=width)

plt.title("Salario promedio de la profesión por edad")
plt.ylabel("Cantidad de edades")
plt.xlabel("Salario medio MUSD")

#plt.xticks(ticks=edad_np_x,labels=edad_x)

plt.grid(True)
plt.legend()

plt.savefig("mi primera gráfica.png")


plt.show()

