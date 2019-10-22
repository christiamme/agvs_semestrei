#!/usr/bin/python3

#===Setup===#
import svgwrite

#===Funciones===#
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
