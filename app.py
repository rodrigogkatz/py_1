#Imports externos
from datetime import date

#Imports internos
import constantes

print("---------------------------------------------")
print("Hola, como estas?")

"""
https://www.youtube.com/watch?v=8DvywoWv6fI&ab_channel=freeCodeCamp.org
https://www.python.org/downloads/
Asi se hacen los comentarios de varias lineas
input() siempre devuelve un string
Si quiero hacer un comment de una sola linea tengo que usar # como en los casos de abajo
"""

# Pedir el nombre y guardarla/o en una variable
nombre = input("Como te llamas? ")
while len(nombre) <= constantes.MINNOMBRE or nombre.isalpha() == False:
	print("ERROR: El nombre debe tener caracteres alfabeticos y debe tener mas de dos caracteres")
	nombre = input("Reingrese su nombre: ")

# Pedir la edad y guardarla/o en una variable
edad = int(input("Cuantos años tenes? "))
while type(edad) != int or edad < constantes.MINEDAD:
	print("ERROR: La edad debe ser un numero entero. Y debe ser mayor de edad")
	edad = int(input("Reingrese su edad: "))

# Pedir el dia de nacimiento y guardarla/o en una variable
diaDeNacimiento = int(input("Dia de nacimiento: "))
while type(diaDeNacimiento) != int or diaDeNacimiento < constantes.UNO or diaDeNacimiento > constantes.MAXDIA:
	print("ERROR: El dia debe ser un numero entero entre 1 y 31")
	diaDeNacimiento = int(input("Reingrese el dia de nacimiento: "))

# Pedir el mes de nacimiento y guardarla/o en una variable
mesDeNacimiento = int(input("Mes de nacimiento: "))
while type(mesDeNacimiento) != int or mesDeNacimiento < constantes.UNO or mesDeNacimiento > constantes.MAXMES:
	print("ERROR: El mes debe ser un numero entero entre 1 y 12")
	mesDeNacimiento = int(input("Reingrese el mes de nacimiento: "))

anoActual = date.today().year
mesActual = date.today().month
diaActual = date.today().day

print("---------------------------------------------")
print("    Hoy es el dia " + str(diaActual) + ", del mes " + str(mesActual) + ", año " + str(anoActual))
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
