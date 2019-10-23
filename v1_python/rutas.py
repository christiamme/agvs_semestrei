#!/usr/bin/python3

#===Setup===#
import svgwrite
import math
#Configuración del dibujo de las rutas
#agvs_etiqueta = []
#agvs_color = []

#===Funciones===#
#Mapa de rutas
#agrega_ruta recibe punto inicial y punto final de la línea a dibujar
def agrega_ruta( p1, p2):
	dwg = svgwrite.Drawing('test.svg', profile='tiny')
	dwg.add(dwg.line(p1, p2, stroke=svgwrite.rgb(10, 10, 16, '%')))
	dwg.add(dwg.text('Test', insert=(0, 0.2), fill='red'))
	dwg.save()
	return
#Cambio en el ángulo a partir de la dirección dada
def angulo(ang,dir):
    if dir=="NN":
        ang+=0
    elif dir=="NE":
        ang-=math.pi/4
    elif dir=="EE":
        ang-=math.pi/2
    elif dir=="SE":
        ang-=3*math.pi/4
    elif dir=="SD":
        ang-=math.pi
    elif dir=="GD":
        ang-=2*math.pi
    elif dir=="NO":
        ang+=math.pi/4
    elif dir=="OO":
        ang+=math.pi/2
    elif dir=="SO":
        ang+=3*math.pi/4
    elif dir=="SI":
        ang+=math.pi
    elif dir=="GI":
        ang+=2*math.pi
    return ang
#Cálculo de posición final a partir del punto inicial y la distancia recorrida
def pos_final ( inicial, direccion, distancia ):
	theta=round(angulo(inicial[2],direccion),6)
	xf=round(inicial[0]+int(distancia)*math.sin(theta),2)
	yf=round(inicial[1]+int(distancia)*math.cos(theta),2)
	pos_fin=[xf,yf,theta]
	return pos_fin
