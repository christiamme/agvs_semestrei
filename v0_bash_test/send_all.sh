#!/bin/bash

#Direcciones IP de los AGVs
agvs=("localhost" "192.168.137.197")

#Notificación de inicio de envío
echo "Datos a enviar: "
cat instrucciones.txt
echo "Inicia envío..."

#Envío de datos
for agv in ${agvs[@]}
do
	cat instrucciones.txt | nc "$agv" 9230 -w 1
	#Mensaje de envío
	echo "Enviado a $agv"
done

