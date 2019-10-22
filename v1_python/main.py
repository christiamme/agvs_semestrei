#!/usr/bin/python3

#===Setup===#
import agvsend
import rutas

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

#===Main===#
#Formato de la instrucción es "BC /NN+00WC "
mensaje = "BC / NN+20WC "
#agvsend.send_to_agv(mensaje,agvs[0])
inicial=(0,0)
final=(50,50)
rutas.agrega_ruta(inicial,final)
