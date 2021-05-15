import numpy as np
import matplotlib.pyplot as plt
import random
#Definición de variables globales
m = 2**32
a = 1013904223
c = 1664525
x0 = (102264 + 102425 + 104112)//3

def gcl(n): #n = cantidad de iteraciones
	valores = []
	x_act = x0
	for i in range(n):
		x_sig = (a * x_act + c) % m
		valores.append(x_sig)
		x_act = x_sig
	return valores

def gclB(n): #n = cantidad de iteraciones
	valores_normalizados = gcl(n)
	for i in range(len(valores_normalizados)):
		valores_normalizados[i] = valores_normalizados[i]/m
	return valores_normalizados

def gclD(n,valores): #n = cantidad de iteraciones
	for i in range(n-55):
		x_sig = (valores[i-24] + valores[i-55]) % 2**24
		valores.append(x_sig)
	return valores

def main():
	n=1000
#a) Implementar un Generador Congruencial Lineal (GCL) de módulo 2
#32, multiplicador 1013904223, incremento de
#1664525 y semilla igual a la parte entera del promedio de los números de padrón de los integrantes del grupo.
	a_results = gcl(n)

#b) Modificar el GCL implementado en el punto a) para que devuelva números al azar entre 0 y 1
	b_results = gclB(n)

#c) Realizar los gráficos que considere necesarios para mostrar las distribuciones de números al azar
#generados en los puntos a) y b)
	plt.plot(a_results) #density plot
	plt.show()
	
	plt.plot(b_results) #density plot
	plt.show()

	nums =[]
	for i in range(n):
		nums.append(i)
	plt.scatter(a_results,nums, alpha=0.5) #scatter plot
	plt.show()	
	
	plt.scatter(b_results,nums, alpha=0.5) #scatter plot
	plt.show()

#d) Basándose en el generador implementado en el ítem a,implemente el generador aditivo de Mitchell y Moore
	valores_arbitrarios = []
	for i in range(55):
		valores_arbitrarios.append(random.randint(0, 2**24))
	d_results = gclD(n,valores_arbitrarios)

main()