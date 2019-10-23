#!/usr/bin/python3

#===Setup===#
import agvsend
import rutas
from math import pi

#Direcciones IP de los AGVs
agvs = ["192.168.30.70"]
#Setup AGV
#   * Set de Instrucciones recorrido[]
#   * Posición inicial posini[x-mapa,y-mapa,a-ángulo orientación]
#recorrido[]=[]
pos=[]
pos.append([0,0,pi/2])

#===Main===#
#Formato de la instrucción es "BC /NN+00WC "
print(pos[0])
mensaje = "BC / NN+20WC "
final=rutas.pos_final(pos[0], mensaje[5:7], mensaje[7:10])
print(final)
mensaje = "BC / NE+10WC "
final=rutas.pos_final(final, mensaje[5:7], mensaje[7:10])
print(final)
mensaje = "BC / EE+10WC "
final=rutas.pos_final(final, mensaje[5:7], mensaje[7:10])
print(final)
mensaje = "BC / NE+20WC "
final=rutas.pos_final(final, mensaje[5:7], mensaje[7:10])
print(final)


#rutas.agrega_ruta(inicial,final)
