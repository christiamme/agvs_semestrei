#!/usr/bin/python3

#===Setup===#
import socket
import svgwrite
#Puerto de comunicación elegido
puerto = 9230
#Direcciones IP de los AGVs
agvs = ["localhost", "192.168.30.70"]
#Indicaciones a cada AGV
#agv[]=[]
#agv[]=[]
#agv[]=[]
#agv[]=[]
#agv[]=[]
#agv[]=[]
#Configuración del dibujo de las rutas
#agvs_etiqueta = []
#agvs_color = []
#agvs_pos_ini = []

#===Funciones===#
#Envío de instrucciones
def send_to_agv( instr, ip ):
	#Abre conexión
	s = socket.socket()   
	s.connect((ip, puerto))
	#Envío de la instrucción
	s.send(bytes(instr,'utf8'))
	#Confirmación de envío
	print("Instrucción enviada")
	#Cierre del puerto
	s.close()
	return
#Mapa de rutas
def agrega_ruta( p1, p2):
	dwg = svgwrite.Drawing('test.svg', profile='tiny')
	dwg.add(dwg.line(p1, p2, stroke=svgwrite.rgb(10, 10, 16, '%')))
	dwg.add(dwg.text('Test', insert=(0, 0.2), fill='red'))
	dwg.save()
	return
#Cálculo de posición final
def pos_final ( pin, vec ):
	
	return

#===Main===#
#Formato de la instrucción es "BC /NN+00WC "
mensaje = "BC / NN+20WC "
#send_to_agv(mensaje,agvs[0])
inicial=(0,0)
final=(50,50)
agrega_ruta(inicial,final)