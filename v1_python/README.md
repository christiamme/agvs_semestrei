# AGV Broadcast Communications with Python3 - Semestre i IMT (MR WAS)

Send commands to multiple AGVs via a TCP/IP socket. The AGVs are using [NXP's S32K144 Evaluation Board] (https://www.nxp.com/design/development-boards/automotive-development-platforms/s32k-mcu-platforms/s32k144-evaluation-board:S32K144EVB). Make the AGVS dance!!

## Getting Started



### Pre-requisites

The code requires `python3` and the following modules:

```
socket
svgwrite
```

### Installing



## Deployment

The instruction set corresponds with the following document (in Spanish):

Se recomienda contar con una instrucción que cambie la conexión entre la necesaria para la aplicación móvil (p.e. una conexión directa a un dispositivo móvil) y la conexión a la red de broadcast (SSID Semestre_i, WPA Semestre_i).

La instrucción de broadcast será un string con el formato "BC /NN+00WC ".
	* 4 caracteres de inicio de instrucción de broadcast ("BC /")
	* 2 caracteres indicadores de posicionamiento (11 posiciones posibles, ver lista)
	* 1 caracter indicador de dirección ("+" para frente, "-" para reversa)
	* 2 dígitos para indicar el número de pasos, de 20 cm cada uno, desde 00 hasta 99
	* 1 caracter para indicar movimiento de la mesa ("M" para subir mesa, "W" para bajar mesa)
	* 1 caracter para indicar modo ("C" para continuar esperando otra instrucción en modo broadcast, "R" para regresar al modo app)
	* 1 caracter de espacio para indicar fin de instrucción

El posicionamiento que el vehículo debe tomar antes de avanzar está dado por la siguiente tabla.
	Mantener posición
		* NN: Avanzar o retroceder sin girar
	Giros a la derecha
		* NE: Girar 45° antes de avanzar
		* EE: Girar 90° antes de avanzar
		* SE: Girar 135° antes de avanzar
		* SD: Girar 180° antes de avanzar
		* GD: Girar 360° antes de avanzar
	Giros a la izquierda
		* NO: Girar 45° antes de avanzar
		* OO: Girar 90° antes de avanzar
		* SO: Girar 135° antes de avanzar
	  * SI: Girar 180° antes de avanzar
		* GI: Girar 360° antes de avanzar

## Built With

* [python3](https://www.python.org/downloads/) - Version 3.6.5
* [svgwrite](https://pypi.org/project/svgwrite/) - Version 1.3.1

## Contributing



## Versioning



## Author

* **Christiam Mendoza** - *Initial work* - [ChristiamME](https://github.com/christiamme)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

*
