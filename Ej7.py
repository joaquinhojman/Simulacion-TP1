''' 
N: cantidad de individuos en la población.
El area mide 100 m x 100 m, y cada persona "ocupa" 0.5 m x 0.5 m
---> El espacio tiene 200 celdas de largo y 200 de ancho. (40 000 celdas)

Inicialmente el 2% de los N individuos esta infectado.
Hay tres tipos de individuos:
	-A: (70%) se desplaza 1 celda en 1 instante de t.
	-B: (25%) se desplaza 1 celda en 2 instantes de t.
	-C: (5%) se desplaza 1 celda en 4 instantes de t.

La probabilidad de transmitir la enfermedad es:
	-0.5 cuando la dist es entre 6 o menos celdas y mas de 3
	-0.7 cuando la dist es entre 3 o menos celdas

Supongo que los individuos unicamente se mueven hacia los costados o arriba y abajo. No en diagonal.
Se modelan los espacios en blanco como _, los espacios con infectados como X, y los sanos como O.
'''
import matplotlib.pyplot as plt
import random
n = 500 #cantidad de individuos en la poblacion
NCELDASXFILA = 100

def generar_espacio_vacio():
	espacio = []
	for i in range(NCELDASXFILA):
		fila = []
		for j in range(NCELDASXFILA):
			fila.append("_")
		espacio.append(fila)
	return espacio

def obtener_estado(personas):
	espacio = generar_espacio_vacio()
	for v in personas.values():
		espacio[v[0]][v[1]] = v[2]
	return espacio

def imprimir_estado(personas):
	print(obtener_estado(personas))
	print("")

def hay_movimiento(tipo):
	if (tipo == "A"):
		return True
	probMovimiento = random.random()
	if (tipo == "B" and probMovimiento <= 0.5):
		return True
	if (tipo == "C" and probMovimiento <= 0.25):
		return True
	return False

def verificar_rango(i,j,dist):
	if (i + dist < 0 or i + dist >= NCELDASXFILA):
		return False
	if (j + dist < 0 or j + dist >= NCELDASXFILA):
		return False
	return True

def verificar_si_se_infecta(espacio,j,i):
	for dist in range(-3,3):
		if (verificar_rango(i,j,dist) == False):
			continue
		if (espacio[j][i+dist] == "X" or espacio[j+dist][i] == "X"):
			probContagio = random.random()
			if (probContagio <= 0.7):
				return True

	for dist in range(-6,-4):
		if (verificar_rango(i,j,dist) == False):
			continue
		if (espacio[j][i+dist] == "X" or espacio[j+dist][i] == "X"):
			probContagio = random.random()
			if (probContagio <= 0.5):
				return True

	for dist in range(4,6):
		if (verificar_rango(i,j,dist) == False):
			continue
		if (espacio[j][i+dist] == "X" or espacio[j+dist][i] == "X"):
			probContagio = random.random()
			if (probContagio <= 0.5):
				return True
	return False

def random_walking(personas, contagiados):
	lista_contagios_por_t = []
	lista_sanos_por_t = []
	lista_contagios_por_t.append(contagiados)
	lista_sanos_por_t.append(n-contagiados)
	for instante in range(1000):
		imprimir_estado(personas)
		for k,v in personas.items():
			if (hay_movimiento(v[3]) == False):
				continue
			movimiento = random.random()
			if (movimiento <= 0.25): #sentido del movimiento
				if (v[1]+1 == NCELDASXFILA): #que no se salga de rango
					continue
				personas[k] = (v[0],v[1]+1,v[2],v[3])
			elif (movimiento <= 0.5): #sentido del movimiento
				if (v[1]-1 < 0): #que no se salga de rango
					continue
				personas[k] = (v[0],v[1]-1,v[2],v[3])
			elif (movimiento <= 0.75): #sentido del movimiento
				if (v[0]+1 == NCELDASXFILA): #que no se salga de rango
					continue
				personas[k] = (v[0]+1,v[1],v[2],v[3])
			else: #sentido del movimiento
				if (v[0]-1 < 0): #que no se salga de rango
					continue
				personas[k] = (v[0]-1,v[1],v[2],v[3])

			estado = obtener_estado(personas)
			for i in range(NCELDASXFILA):
				for j in range(NCELDASXFILA):
					if (estado[j][i] == "_" or estado[j][i] == "X"):
						continue
					if (verificar_si_se_infecta(estado,j,i) == True):
						estado[j][i] = "X"
						contagiados += 1
						for k,v in personas.items():
							if (v[0] == j and v[1] == i):
								personas[k] = (v[0],v[1],"X",v[3])
		lista_contagios_por_t.append(contagiados)
		lista_sanos_por_t.append(n-contagiados)
		if (contagiados > 0.9*n):	
			return lista_contagios_por_t,lista_sanos_por_t				
	return lista_contagios_por_t,lista_sanos_por_t				

def estado_inicial(espacio):	
	#Ubico a las N personas de forma aleatoria. El 2% estan infectados.
	#Se decide el "tipo" de persona
	personas = {} #clave: persona. valor: x,y,infectado o no, tipo de persona
	contagiados = 0
	for i in range(n):
		x = random.randrange(0,NCELDASXFILA-1)
		y = random.randrange(0,NCELDASXFILA-1)
		if (espacio[x][y] != "_"):
			i -= 1 #ese espacio estaba ubicado, prueba otra vez en la prox iteracion
			continue 

		tipo = ""
		probTipo = random.random()
		if (probTipo <= 0.70):
			tipo = "A"
		elif (probTipo <= 0.95):
			tipo = "B"
		else:
			tipo = "C"

		probInfectado = random.random()
		if (probInfectado <= 0.02):
			personas[i] = (x,y,"X",tipo)
			espacio[x][y]= "X"
			contagiados += 1
		else:
			personas[i] = (x,y,"O",tipo)
			espacio[x][y] = "O"
	return personas, contagiados

def main():	
	#Genero el espacio vacio
	espacio = generar_espacio_vacio()
	
	personas, contagiados = estado_inicial(espacio)

	lista_contagiados, lista_sanos = random_walking(personas,contagiados)

#	plt.plot(lista_contagiados);
#	plt.show()

#	print(len(lista_contagiados))
	#3 instantes de tiempo siendo n=2000
	#5 instantes de tiempo siendo n=1000
	#25 instantes de tiempo siendo n=500
	#211 instantes de tiempo siendo n=250
	#733 instantes de tiempo siendo n=100
#	x = [3,5,25,211,733]
#	y = [2000,1000,500,250,100]
#	plt.scatter(x,y)
#	plt.show()

#	plt.plot(lista_sanos);
#	plt.show()


main()