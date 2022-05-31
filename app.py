#Imports externos
from datetime import date
from datetime import datetime

#Imports internos
import constantes

def mensajear(mensaje):
	print("---------------------------------------------")
	print(mensaje)

#esta funcion deberia ser privada
def formatearString(textoParaFormatear, tipoDeTexto):
	textoParaFormatear = textoParaFormatear.capitalize()
	if tipoDeTexto == "fecha":
		return textoParaFormatear[0:3]
	if tipoDeTexto == "generico":
		return textoParaFormatear

#esta funcion deberia ser privada
def agregarCeroIzq(numero):
	resultado = numero
	if int(numero) < 10 and int(numero) >= 0:
		resultado = "0" + numero
	return resultado

def imprimirResultados(diaActual, mesActual, minMes, maxMes, mensajeDeErrorMes, anoActual, horaActual, minutoActual, segundoActual, nombre, appellido, diaDeNacimiento, mesDeNacimiento, edad):
	print("---------------------------------------------")
	print("    Hoy es el dia " + str(diaActual) + " de " + definirMes(mesActual, constantes.UNO, constantes.MAXMES, mensajeDeErrorMes) + " del año " + str(anoActual))
	print("    Hora " + agregarCeroIzq(str(horaActual)) + ":" + agregarCeroIzq(str(minutoActual)) + ":" + agregarCeroIzq(str(segundoActual)))
	print("---------------------------------------------")
	print("\tBuen dia " + formatearString(apellido, "generico") + ", " + formatearString(nombre, "generico"))
	anoDeNacimiento = calcularAnoDeNacimiento(diaDeNacimiento, mesDeNacimiento, edad, diaActual, mesActual, anoActual)
	print("\tNaciste en la fecha " + str(diaDeNacimiento) + "/" + str(mesDeNacimiento) + "/" + str(anoDeNacimiento))
	print("---------------------------------------------")

def calcularAnoDeNacimiento(diaDeNacimiento, mesDeNacimiento, edad, diaActual, mesActual, anoActual):
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
	return anoDeNacimiento

def pedirCodigoDeDesbloqueo(mensajeDeDesbloqueo, errorCodigoDeDesbloque, mensajeDesbloqueoSatisfactorio):
	resultado = 1
	codigoDeDesbloqueo = input(mensajeDeDesbloqueo)
	while (len(codigoDeDesbloqueo) > 14 or len(codigoDeDesbloqueo) < 14) and codigoDeDesbloqueo != "Desbloqueo1234":
		resultado = -1
		codigoDeDesbloqueo = input(errorCodigoDeDesbloqueo)
	if resultado == -1:
		print(errorCodigoDeDesbloqueo)
	elif resultado == 1:
		print(mensajeDesbloqueoSatisfactorio)
	return resultado

def pedirDato(tipoDeDato, primeraPregunta, minDato, maxDato, mensajeDeError, preguntaDespuesDeError, reintentos, reintentosError, codigoDeDesbloqueo):
	if tipoDeDato == 'string':
		dato = input(primeraPregunta)
		while len(dato) <= minDato or dato.isalpha() == False:
			if reintentos > 0:
				print(mensajeDeError)
				reintentos = reintentos - constantes.UNO
				print(tipoDeDato + ": " + str(reintentos) + " " + reintentosError)
				dato = input(preguntaDespuesDeError)
			if reintentos < 0:
				reintentos = 3
				resultado = pedirCodigoDeDesbloqueo("Ingrese el codigo de desbloqueo para continuar (Desbloqueo1234): ", "El codigo de debloqueo no funciona, contacte al administrador del sitema... JODETE HERMANO", "El flujo fue desbloqueado")	
		return dato
	if tipoDeDato == 'entero':
		dato = int(input(primeraPregunta))
		while type(dato) != int or dato < minDato or dato > maxDato:
			if reintentos > 0:
				print(mensajeDeError)
				reintentos = reintentos - constantes.UNO
				print(tipoDeDato + ": " + str(reintentos) + " " + reintentosError)
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
		mes = "oCTubre"
	elif numeroDeMes == 11:
		mes = "noviembre"
	elif numeroDeMes == 12:
		mes = "diciembre"
	return formatearString(mes, "fecha")

"""
https://www.youtube.com/watch?v=8DvywoWv6fI&ab_channel=freeCodeCamp.org
https://www.python.org/downloads/
Asi se hacen los comentarios de varias lineas
input() siempre devuelve un string
Si quiero hacer un comment de una sola linea tengo que usar # como en los casos de abajo
"""

anoActual = date.today().year
mesActual = date.today().month
diaActual = date.today().day

#horarioActual = now.strftime("%H:%M:%S")
horaActual = datetime.now().hour
minutoActual = datetime.now().minute
segundoActual = datetime.now().second

mensajear("Ingrese los siguientes datos:")
nombre = pedirDato("string", "Nombre: ", constantes.MINNOMBRE, constantes.MAXNOMBRE, "ERROR: El nombre debe tener caracteres alfabeticos y debe tener entre 2 y 150 caracteres", "Ingrese nuevamente su nombre: ", constantes.REINTENTOS, "reintentos disponibles", "Desbloqueo1234")
apellido = pedirDato("string", "Apellido: ", constantes.MINNOMBRE, constantes.MAXNOMBRE, "ERROR: El apellido debe tener caracteres alfabeticos y debe tener entre 2 y 150 caracteres", "Ingrese nuevamente su apellido: ", constantes.REINTENTOS, "reintentos disponibles", "Desbloqueo1234")
edad = pedirDato("entero", "Edad: ", constantes.MINEDAD, constantes.MAXEDAD, "ERROR: La edad debe ser un numero entero. Y debe ser mayor de 18 y menor de 120", "Ingrese nuevamente su edad: ", constantes.REINTENTOS, "reintentos disponibles", "Desbloqueo1234")
diaDeNacimiento = pedirDato("entero", "Dia de nacimiento: ", constantes.UNO, constantes.MAXDIA, "ERROR: El dia debe ser un numero entero entre 1 y 31", "Ingrese nuevamente el dia de nacimiento: ", constantes.REINTENTOS, "reintentos disponibles", "Desbloqueo1234")
mesDeNacimiento = pedirDato("entero", "Mes de nacimiento: ", constantes.UNO, constantes.MAXMES, "ERROR: El mes debe ser un numero entero entre 1 y 12", "Ingrese nuevamente el mes de nacimiento: ", constantes.REINTENTOS, "reintentos disponibles", "Desbloqueo1234")

mensajear("Resultados:")
imprimirResultados(diaActual, mesActual, constantes.UNO, constantes.MAXMES, "ERROR: El mes debe ser un numero entero entre 1 y 12", anoActual, horaActual, minutoActual, segundoActual, nombre, apellido, diaDeNacimiento, mesDeNacimiento, edad)


