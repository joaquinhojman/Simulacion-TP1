#Implemente un método para generar variables aleatorias con distribución normal con media 15 y desvío 3.
#Muestre gráficamente la distribución que siguen los números pseudoaleatorios generados.
#Realice 2 tests de los explicados en la materia para verificar si los números generados siguen la distribución pedida (evalué los
#resultados para distintos tamaños de muestra).


#CREO QUE ESTO SE HACE CON EL METODO ACEPTACION-RECHAZO. LO INTENTO IMPLEMENTAR AHORA.
#LAS FUNCIONES QUE GENERAN LA NORMAL LO SAQUE DEL TP DE AZU.

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import random as rn
import math


def generate_normal_acceptance_rejection(n, mu, sigma, output):
    numbers = generate_standard_normal_acceptance_rejection(n, output)
    return (numbers * sigma) + mu


def generate_standard_normal_acceptance_rejection(n, output):
    c = 2 * stats.norm.pdf(1) / stats.expon.pdf(1)

    numbers = np.array([])
    accepted_n, rejected_n = 0, 0
    while accepted_n < n:
        x = np.random.exponential()
        p = stats.norm.pdf(x) / (c * stats.expon.pdf(x))
        y = rn.random()

        if y <= p:
            r1 = rn.random()
            if r1 < 0.5:
                numbers = np.append(numbers, x)
            else:
                numbers = np.append(numbers, -x)

            accepted_n += 1
            continue
        else:
            rejected_n += 1

    total_n = accepted_n + rejected_n
    rejection_percentage = rejected_n * 100 / total_n

    return numbers


def draw_histogram(numbers, show):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.hist(numbers, weights=np.zeros_like(numbers) + 1.0 / numbers.size, bins=20)
    if show:
        plt.show()


# Implemente un método para generar variables aleatorias con distribución normal con media 15 y desvío 3.
#n, mu, sigma = 100000, 15, 3
print("Cantidad de números a generar={}".format(n))
print("Distribución Normal(mu={},sigma={})".format(mu, sigma))
#numbers = generate_normal_acceptance_rejection(n, mu, sigma, True)

# Muestre gráficamente la distribución que siguen los números pseudoaleatorios generados.
draw_histogram(numbers, True)

#Realice 2 tests de los explicados en la materia para verificar si los números generados siguen la distribución pedida (evalué los
#resultados para distintos tamaños de muestra).

#Realizo test de Kolgomorov-Smirnov
def test_normal_kolmogorov_smirnov(numbers_per_test, mu, sigma, alpha, output):
    print("Hago el test Kolgomorov Smirnov con una muestra de {} ",numbers_per_test)
    
    numbers = generate_normal_acceptance_rejection(numbers_per_test, mu, sigma, True)

    resultado = stats.kstest(numbers, stats.norm(mu,sigma).cdf)

    if (resultado.pvalue < alpha):
		    print("No siguen la distribucion pedida")
    else:
        print("Los datos siguen la distribucion pedida")
    print(" ")
	
def test_normal_anderson(numbers_per_test, mu, sigma, output):
    print("Hago el test Anderson-Darling con una muestra de {} ",numbers_per_test)
    
    numbers = generate_normal_acceptance_rejection(numbers_per_test, mu, sigma, True)

    resultado = stats.anderson(numbers)

    for i in range(len(resultado.critical_values)):
        nivel_significancia, umbral = resultado.significance_level[i]/100, resultado.critical_values[i]
        if resultado.statistic < resultado.critical_values[i]:
            print('%.3f: %.3f, Datos normales (No se puede rechazar H0)' % (nivel_significancia, umbral))
        else:
            print('%.3f: %.3f, Datos No normales (Se rechaza H0)' % (nivel_significancia, umbral))


alpha = 0.01
numbers_per_test_1 = 100
numbers_per_test_2 = 1000
numbers_per_test_3 = 10000
numbers_per_test_4 = 100000

print(" ")
print(" ")
test_normal_kolmogorov_smirnov(numbers_per_test_1, mu, sigma, alpha, True)
test_normal_kolmogorov_smirnov(numbers_per_test_2, mu, sigma, alpha, True)
test_normal_kolmogorov_smirnov(numbers_per_test_3, mu, sigma, alpha, True)
test_normal_kolmogorov_smirnov(numbers_per_test_4, mu, sigma, alpha, True)
print(" ")
print(" ")
test_normal_anderson(numbers_per_test_1,mu,sigma,True)
test_normal_anderson(numbers_per_test_2,mu,sigma,True)
test_normal_anderson(numbers_per_test_3,mu,sigma,True)
test_normal_anderson(numbers_per_test_4,mu,sigma,True)
