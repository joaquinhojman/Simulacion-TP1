import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from Ej1 import gcl, gclB,gclD
#2)Para cada uno de los generadores del ejercicio 1, proponer, y realizar, al menos 2 tests para evaluar su
#comportamiento. Evaluar e interpretar los resultados de cada uno para distintos tamaños de muestras.
m = 2**32

#LEER ABAJO, EN RESULTADOS OBTENIDOS, COMO PROBAR CADA GENERADOR

def gapTest(nGaps,alpha,beta):
	i = 0
	gap = 0
	gaps = np.zeros(nGaps)
	number = gcl(1)[0]
	while i < nGaps:
		if((number > alpha) and (number <= beta)):
			gap += 1
		else:
			np.append(gaps, gap + 1)
			gaps[i] = gap + 1
			i += 1
			gap = 0
		number_gcl = gcl(1, x0 = number)[0]
		number = gcl(1, x0 = number_gcl)[0]

	p = (beta - alpha)
	expected = np.zeros(nGaps)
	for j in range(len(gaps)):
		num = gaps[j]
		expected[j] = p*((1-p)**(num-1))*(nGaps)
	[h,pValor] = stats.chisquare(gaps, expected)
	return pValor

def main():
	#Test 1: GapTest
	#Se toma alpha = 0.3, beta = 0.6.
	pValor= gapTest(13, 0.2, 0.5)
	nivelDeSignifiacion = 0.01
	if pValor < nivelDeSignifiacion:
	    print("El test rechaza la hipotesis nula")
	else:
	    print("El test acepta la hipotesis nula")

main()

'''RESULTADOS OBSERVADOS: alpha = 0.3, beta = 0.6. n de sign = 0.01

Para el generador A: (multiplicar alpha y beta por m. Dividir p por m (linea 25))
nGaps = 12 o menor: acepta
nGaps = 13 o mayor: rechaza

Para el generador B: (la linea 22 multiplicarla por m = 2**32)
nGaps = 10 o menor: acepta
nGaps = 11 o mayor: rechaza

Para el generador D: (multiplicar alpha y beta por m=2**24. Dividir p por m (linea 25))
nGaps = 13 o menor: acepta
nGaps = 14 o mayor: rechaza

'''