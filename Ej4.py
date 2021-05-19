#Para la siguiente funcion:
#A) Definir su funcion de densidad de probabilidad
#B) Calcular y graficar la funcion de probabilidad acumulada y su inversa
#C) Utilizando el generador de numero aleatorios implementado en el item b 
#   del ejercicio 1, genere numeros al azar con la distribucion propuesta
#D) Realice los graficos que considere necesarios para mostrar la distribucion
#   de numeros al azar generados.
 
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import random


#--------------EJERCICIO A-----------------#
# Calculado a mano en el cuaderno.
# Como es una funcion definida a trozos debo definir todas sus terminos por separado
# Funcion densidad entera es:
# (1/15)*x - 1/5 1{1<x<4} + (-2/45)*x + 17/45 1{4<x<6} + 1/9 1{6<x<9} + (-1/9)*x + 10/9 1{9<x<10}

#f es mi funcion y f0,f1,..fn son los terminos

x0 = np.linspace(0, 1) 
f0 = np.piecewise(x0, [x0>=0], [lambda x0: 0])

x1 = np.linspace(1, 4) 
f1 = np.piecewise(x1, [x1>=1], [lambda x1: (1/15)*x1 - 1/15])

x2 = np.linspace(4, 6) 
f2 = np.piecewise(x2, [x2>=4], [lambda x2: (-2/45)*x2 + 17/45])

x3 = np.linspace(6, 9) 
f3 = np.piecewise(x3, [x3>=6], [lambda x3: 1/9])

x4 = np.linspace(9, 10) 
f4 = np.piecewise(x4, [x4>=9], [lambda x4: (-1/9)*x4 + 10/9])

# Grafico.

plt.plot(x0, f0)
plt.plot(x1, f1)
plt.plot(x2, f2)
plt.plot(x3, f3)
plt.plot(x4, f4)

plt.title('Función de densidad')
plt.show()

#--------------EJERCICIO B-----------------#
#Para calcular la función de probabilidad acumulada o función de distribución, se integró la función de densidad
#entre menos infinito y X.

#Pongo los links a wolfram alpha para corroborar las cuentas. Luego defino las acumuladas como hice
#con las densidades.

#F es mi funcion y F0,F1,..Fn son los terminos

x0 = np.linspace(0, 1) 
F0 = np.piecewise(x0, [x0>=0], [lambda x0: 0])

#https://www.wolframalpha.com/input/?i=integral+from+1+to+x+of+%281%2F15%29*x+-+1%2F15
x1 = np.linspace(1, 4) 
F1 = np.piecewise(x1, [x1>=1], [lambda x1: 1/30 * (-1 + x1)**2])

#https://www.wolframalpha.com/input/?i=integral+from+4+to+x+of+%28-2%2F45%29*x+%2B+17%2F45
x2 = np.linspace(4, 6) 
F2 = np.piecewise(x2, [x2>=4], [lambda x2: 1/45 *(-52 + 17 * x2 - x2**2) + 0.3])

#https://www.wolframalpha.com/input/?i=integral+from+6+to+x+of+1%2F9
x3 = np.linspace(6, 9) 
F3 = np.piecewise(x3, [x3>=6], [lambda x3: (x3-6)/9 + 0.611111])

#https://www.wolframalpha.com/input/?i=integral+from+9+to+x+of+%28-1%2F9%29*x+%2B+10%2F9
x4 = np.linspace(9, 10) 
F4 = np.piecewise(x4, [x4>=9], [lambda x4: 1/18 * (-99 + 20*x4 - x4**2) + 0.944433333])

plt.plot(x0, F0)
plt.plot(x1, F1)
plt.plot(x2, F2)
plt.plot(x3, F3)
plt.plot(x4, F4)

plt.title('Función de distribucion acumulada')
#ACLARACION, cuando se agrega el termino sumando a las funciones F2, F3 y F4 es para que la funcion "acumule".
plt.show()

#Realizo la interpolacion. Para calcular la funcion inversa.
x1,F1 = F1,x1
F1_inversa = interpolate.interp1d(x1,F1)
plt.plot(x1, F1, x1, F1_inversa(x1),'-')

x2,F2 = F2,x2
F2_inversa = interpolate.interp1d(x2,F2)
plt.plot(x2, F2, x2, F2_inversa(x2),'-')

x3,F3 = F3,x3
F3_inversa = interpolate.interp1d(x3,F3)
plt.plot(x3, F3, x3, F3_inversa(x3),'-')

x4,F4 = F4,x4
F4_inversa = interpolate.interp1d(x4,F4)
plt.plot(x4, F4, x4, F4_inversa(x4),'-')

plt.title('Función de distribución inversa')
plt.show()

#--------------EJERCICIO C y D-----------------#
#Uso la funcion de joaco del punto 1b, deberia ir un import en el codigo posta.
from Ej1 import gclB

def funcion(x):
  y = []
  for i in range(len(x)):
    if(x[i]<0.3):
      y.append(F1_inversa(x[i]))
    elif(x[i]<0.61111):
      y.append(F2_inversa(x[i]))
    elif(x[i]<0.944433333):
      y.append(F3_inversa(x[i]))
    elif(x[i]<1):
      y.append(F4_inversa(x[i]))
  return y


x_new = gclB(1000)
y_new = funcion(x_new)
plt.hist(y_new)
plt.title('Histograma')
plt.show() 
