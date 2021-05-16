import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2
import collections
from Ej1 import gcl, gclB,gclD
#2)Para cada uno de los generadores del ejercicio 1, proponer, y realizar, al menos 2 tests para evaluar su
#comportamiento. Evaluar e interpretar los resultados de cada uno para distintos tamaños de muestras.

#Se realiza un test de frecuencia.
def testFrecuencias(n,m,generador):
	pE = 1/m #prob de salir de cada numero
	fEsp = n*pE #frecuencia esperada de cada uno
	nros = collections.Counter(generador(n,m=m))
	dcuad = 0
	for i in range(m):
		print(i)
		dcuad += ((nros[i]-fEsp)**2)
	dcuad = dcuad/fEsp
	print("Dcuad: "+str(dcuad))
	limiteSuperior = chi2.ppf(0.99, df=m)
	print("limiteSuperior: "+str(limiteSuperior))
	if (dcuad <= limiteSuperior):
		print("El test acepta la hipotesis nula")
	else:
		print("El test rechaza la hipotesis nula")


def main():
	#para GCL del punto A:
	#testFrecuencias(100,2**32,gcl)
	#con 1000 y 0.95 acepta
	#con 1000 y 0.99 acepta
	#con 10000 y 0.99 acepta
	#con 100000 y 0.99 acepta
	#con 100 y 0.99 acepta

	#para GCL del punto B
	#testFrecuencias(1000,2**32,gclB)
	#con 1000 y 0.95 acepta
	#con 1000 y 0.99 acepta
	#con 10000 y 0.99 acepta
	#con 100000 y 0.99 acepta
	#con 100 y 0.99 acepta

	#para GCL del punto D
	#testFrecuencias(100000,2**24,gclD)
	#con 1000 y 0.95 rechaza
	#con 1000 y 0.99 rechaza
	#con 10000 y 0.99 rechaza
	#con 100000 y 0.99 acepta

main()