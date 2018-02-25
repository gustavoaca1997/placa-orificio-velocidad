# Script para obtener la velocidad de una placa orificio mediante tanteos
Script en Python3 para obtener la velocidad de una placa orificio mediante tanteos, guardando en un archivo _output.txt_ los resultados.
## Uso
`python tanteo.py <n>`
1. `<n>`: Número de velocidades a calcular.

### Parametros
Se debe guardar en un archivo de texto llamado _input.txt_ los parametros para el tanteo con el siguiente formato:
```
Semilla: <velocidad semilla>
D: <diametro de la partícula>
miu: <coeficiente de biscosidad>
beta: <elación entre los diametros de la placa orificio>
Ad: <Área de la garganta de la placa orificio>
AD: <Áera de la tubería>
Tolerancia: <tolerancia>
Densidad: <densidad 1>
Densidad: <densidad 2>
.
.
.
Densidad: <densidad n>
Caída de Presión: <caida de presión 1>
Caída de Presión: <caída de presion 2>
.
.
.
Caída de Presión: <caída de presion n>
```
_n_ del _input.txt_ debe coincidir con `<n>`