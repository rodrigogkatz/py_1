#Imports externos
from datetime import date
from datetime import datetime

#Imports internos
import constantes

print("---------------------------------------------")
print("Hola, buen dia")

"""
https://www.youtube.com/watch?v=8DvywoWv6fI&ab_channel=freeCodeCamp.org
https://www.python.org/downloads/
Asi se hacen los comentarios de varias lineas
input() siempre devuelve un string
Si quiero hacer un comment de una sola linea tengo que usar # como en los casos de abajo
"""

def pedirDato(tipoDeDato, primeraPregunta, minDato, maxDato, mensajeDeError, preguntaDespuesDeError, reintentos):
	if tipoDeDato == 'string':
		dato = input(primeraPregunta)
		while len(dato) <= minDato or dato.isalpha() == False:
			print(mensajeDeError)
			dato = input(preguntaDespuesDeError)
		return dato
	if tipoDeDato == 'entero':
		dato = int(input(primeraPregunta))
		while type(dato) != int or dato < minDato or dato > maxDato:
			print(mensajeDeError)
			dato = int(input(preguntaDespuesDeError))
		return dato
	#float, double statements

def definirMes(numeroDeMes, minMes, maxMes, mensajeDeError):
	mes = ""
	if numeroDeMes < constantes.UNO or numeroDeMes > constantes.MAXMES:
		print(mensajeDeError)
	elif numeroDeMes == 1:
		mes = "enero"
	elif numeroDeMes == 2:
		mes = "febrero"
	elif numeroDeMes == 3:
		mes = "marzo"
	elif numeroDeMes == 4:
		mes = "abril"
	elif numeroDeMes == 5:
		mes = "mayo"
	elif numeroDeMes == 6:
		mes = "junio"
	elif numeroDeMes == 7:
		mes = "julio"
	elif numeroDeMes == 8:
		mes = "agosto"
	elif numeroDeMes == 9:
		mes = "septiembre"
	elif numeroDeMes == 10:
		mes = "octubre"
	elif numeroDeMes == 11:
		mes = "noviembre"
	elif numeroDeMes == 12:
		mes = "diciembre"
	return mes

nombre = pedirDato("string", "Ingrese su nombre: ", constantes.MINNOMBRE, constantes.MAXNOMBRE, "ERROR: El nombre debe tener caracteres alfabeticos y debe tener entre 2 y 150 caracteres", "Ingrese nuevamente su nombre: ", constantes.REINTENTOS)
edad = pedirDato("entero", "Ingrese su edad: ", constantes.MINEDAD, constantes.MAXEDAD, "ERROR: La edad debe ser un numero entero. Y debe ser mayor de 18 y menor de 120", "Ingrese nuevamente su edad: ", constantes.REINTENTOS)
diaDeNacimiento = pedirDato("entero", "Dia de nacimiento: ", constantes.UNO, constantes.MAXDIA, "ERROR: El dia debe ser un numero entero entre 1 y 31", "Ingrese nuevamente el dia de nacimiento: ", constantes.REINTENTOS)
mesDeNacimiento = pedirDato("entero", "Mes de nacimiento: ", constantes.UNO, constantes.MAXMES, "ERROR: El mes debe ser un numero entero entre 1 y 12", "Ingrese nuevamente el mes de nacimiento: ", constantes.REINTENTOS)

anoActual = date.today().year
mesActual = date.today().month
diaActual = date.today().day

#horarioActual = now.strftime("%H:%M:%S")
horaActual = datetime.now().hour
minutoActual = datetime.now().minute
segundoActual = datetime.now().second

#print("Current Time is :", horarioActual)
print("Current hor is :", horaActual)
print("Current min is :", minutoActual)
print("Current seg is :", segundoActual)

print("---------------------------------------------")
print("    Hoy es el dia " + str(diaActual) + " de " + definirMes(mesActual, constantes.UNO, constantes.MAXMES, "ERROR: El mes debe ser un numero entero entre 1 y 12") + " del año " + str(anoActual) + ".\n\tHora " + str(horaActual) + ":" + str(minutoActual) + ":" + str(segundoActual))
print("---------------------------------------------")
print("\tBuen dia " + nombre)

anoDeNacimiento = 0

# Mes de nacimiento igual al mes actual
if mesDeNacimiento == mesActual: 
	# El mes el igual pero el dia de cumpleaños esta pasando -> saludar
	if diaDeNacimiento == diaActual:
		print("\tFeliz cumple vieja!!! Sale alta joda")
		anoDeNacimiento = anoActual - edad

	# El mes el igual pero el dia de cumpleaños no paso -> ya cumpli años
	if diaDeNacimiento < diaActual:
		cuentaPasada = diaActual - diaDeNacimiento
		print("\tFeliz cumple atrasado!!! te deberia haber saludado hace " + str(cuentaPasada) + " dias")
		anoDeNacimiento = anoActual - edad
		
	# El mes el igual pero el dia de cumpleaños ya paso -> no cumpli años
	if diaDeNacimiento > diaActual:
		cuentaRegresiva = diaDeNacimiento - diaActual
		print("\tTe faltan " + str(cuentaRegresiva) + " dias para cumplir años")
		anoDeNacimiento = anoActual - edad - constantes.UNO

# Mes de nacimiento menor al mes actual -> ya cumpli años
if mesDeNacimiento < mesActual:
	anoDeNacimiento = anoActual - edad

# Mes de nacimiento mayor al mes actual -> no cumpli años
if mesDeNacimiento > mesActual:
	anoDeNacimiento = anoActual - edad - constantes.UNO

print("\tNaciste en la fecha " + str(diaDeNacimiento) + "/" + str(mesDeNacimiento) + "/" + str(anoDeNacimiento))
print("---------------------------------------------")
