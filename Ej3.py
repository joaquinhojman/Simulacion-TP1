import numpy as np
import matplotlib.pyplot as plt
import random
from Ej1 import gclB
#Se desea generar puntos al azar con distribución uniforme dentro del área descripta en el gráfico utilizando
#los siguientes generadores de números al azar:

def randomCircle():
	while True:
		x = random.randint(5, 15)
		y = random.randint(5, 15)
		h = (((x-10)**2) + ((y-10)**2))**0.5
		if (h <= 5): #Acepta los valores generados
			return x,y

def gclCircle():
	while True:
		x0 = random.randint(5, 15)
		y0 = random.randint(5, 15)
		x = gclB(1,x0=x0)[0] * 15
		y = gclB(1,x0=y0)[0] * 15
		h = (((x-10)**2) + ((y-10)**2))**0.5
		if (h <= 5): #Acepta los valores generados
			return x,y

def main():
#a) Generadores de números al azar con distribución uniforme, provistos por el lenguaje elegido
	x,y = randomCircle()

#b) Alguno de los generadores de números al azar implementados con el algoritmo del ejercicio 1.
	x,y = gclCircle()

#c) Calcule el factor de rendimiento del método.
'''Los metodos estan diseñados para que siempre devuelvan un numero valido (por el while)
Sin embargo, si les sacamos el while y hacemos n iteraciones, podemos ver cuantos son validos
sobre el total calculado'''

'''Para el generador random del item A, basado en 100.000 iteraciones, el factor de rendimiento es del
67% aproximadamente '''

'''Para el generador del item B, basado en 100.000 iteraciones, el factor de rendimiento es del
32% aproximadamente '''

main()