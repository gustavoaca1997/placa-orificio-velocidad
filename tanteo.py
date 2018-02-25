# Autor: Gustavo Castellanos

import numpy as np
import sys

## Funciones
def dotToComma(numero):
	lista = []
	for c in numero:
		lista.append(c)
	lista[numero.find('.')] = ','

	return "".join(lista)

def error_relativo(x, x_):
	assert(x != 0 or x_ != 0)
	if (x != 0):
		return error_absoluto(x, x_)/abs(x)
	else:
		return error_absoluto(x, x_)/abs(x_)

def error_absoluto(x, x_):
	return abs(x - x_)

## Formulas:
# Numero de Reynolds
def Re(ro, V, D, miu):
	return ro*V*D/miu

# Coeficiente de Arrastre
def Cd(beta, ro, V, D, miu):
	# Constantes de la formula del coeficiente de arrastre
	const = np.float_([0.5961, 0.0261, 0.216, 0.000521, 1e6, 0.0188, 0.0063, 19000, 1e6])

	return const[0] + const[1]*beta*beta - const[2]*np.power(beta, 8) + \
	const[3]*np.power(const[4]*beta/Re(ro, V, D, miu), 0.7) + \
	np.power(beta, 3.5)*(const[5]+const[6]*np.power(const[7]*beta/Re(ro, V, D, miu), 0.8))* \
	np.power(const[8]*beta/Re(ro, V, D, miu), 0.3)

# Caudal de la placa orificio
def Qr(beta, Ad, V, D, miu, delta_p, ro):
	return Ad*Cd(beta, ro, V, D, miu)*np.power(2*delta_p/(ro*(1-0.1894**4)), 0.5)

# Velocidad de la placa orificio
def Vel(beta, Ad, V, D, miu, delta_p, ro, AD):
	return Qr(beta, Ad, V, D, miu, delta_p, ro)/AD

if __name__ == "__main__":
	# Archivo de entrada
	f = open('input.txt', 'r')
	# Archivo de salida
	o = open('output.txt', 'w+')

	# Valores iniciales
	v0, v1 = 0, 0	# velocidades
	ro = 0			# densidad 
	delta_p = 0		# caída de presion
	semilla = np.float_(f.readline().split(': ')[-1])

	# Constantes
	D = np.float_(f.readline().split(': ')[-1])		# Diametro de la partícula
	miu = np.float_(f.readline().split(': ')[-1])	# coeficiente de biscosidad
	beta = np.float_(f.readline().split(': ')[-1])	# relación entre los diametros de la placa orificio
	Ad = np.float_(f.readline().split(': ')[-1])	# Área de la garganta de la placa orificio
	AD = np.float_(f.readline().split(': ')[-1])	# Áerea de la tubería

	# Tolerancia
	TOL = np.float_(f.readline().split(': ')[-1])

	# numero de velocidades a calcular
	n = 16
	if (len(sys.argv) > 1):
		n = int(sys.argv[1])
	# lista de densidades
	densidad = []
	for i in range(n):
		densidad.append(np.float_(f.readline().split(': ')[-1]))
	# lista de delta p
	presion = []
	for i in range(n):
		presion.append(np.float_(f.readline().split(': ')[-1]))

	for i in range(n):
		ro = densidad[i]
		delta_p = presion[i]
		# inicializa velocidades
		v1 = v0 = semilla
		# numero de iteraciones
		iters = 0
		while(iters == 0 or ( iters > 0 and error_absoluto(v0, v1) > TOL) ):
			#print('\t', v1)
			v0 = v1
			v1 = Vel(beta, Ad, v0, D, miu, delta_p, ro, AD)
			iters += 1

		print('Velocidad numero' + str(i+1) + ': ' + str(v1))
		print('\tNumero de iteraciones: ' + str(iters))
		o.write(dotToComma(str(np.around(v1, 5))) + '\r\n')

	f.close()
	o.close()