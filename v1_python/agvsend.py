#!/usr/bin/python3

#===Setup===#
import socket
#Puerto de comunicación elegido
puerto = 9230

#===Funciones===#
#Envío de instrucciones
def send_to_agv( instr, ip ):
	#Abre conexión
	s = socket.socket()
	s.connect((ip, puerto))
	#Envío de la instrucción
	s.send(bytes(instr,'utf8'))
	#Cierre del puerto
	s.close()
	#Confirmación de envío
	return
