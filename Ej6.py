# Kolmogorov Smirnov Test
from numpy.random import randn
from scipy.stats import kstest,uniform, expon, norm
import numpy as np

def main():
#6) Determine, y justifique,a cuál de las siguientes distribuciones pertenecen los números suministrados:
	numeros = []
	f = open("random_numbers.txt", "r")
	for linea in f:
		numeros.append(float(linea.rstrip('\n')))
	f.close()

	umbral = 0.01

	#Test de Uniforme
	print("Prueba de datos uniformes")
	resultado = kstest(numeros,uniform(25,35).cdf)
	if (resultado.pvalue < umbral):
		print("Los datos no son uniformes")
	else:
		print("Los datos son uniformes")
	print("")

	#Test de exponencial
	print("Prueba de datos exponenciales")
	resultado = kstest(numeros,expon(1/30).cdf)
	if (resultado.pvalue < umbral):
		print("Los datos no son exponenciales")
	else:
		print("Los datos son exponenciales")
	print("")

	#Test de normalidad
	print("Prueba de datos normales")
	resultado = kstest(numeros,norm(30,5).cdf)
	if (resultado.pvalue < umbral):
		print("Los datos no son normales")
	else:
		print("Los datos son normales")
	print(resultado)
	print("")

main()