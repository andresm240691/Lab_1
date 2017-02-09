
import csv, operator
import numpy as np
from matplotlib import pyplot as pt



#1) CARGA DE LOS DATOS

#Funcion para leer los archivos csv
def read_file(dir):
	with open(dir) as csvarchivo:
		entrada = csvarchivo.read().splitlines()
		return entrada

# lectura del student-mat
d1 = read_file('C://student-mat.csv')
header = d1.pop(0)
		
#lectura del student-por
d2 = read_file('C://student-por.csv')
d2.pop(0)

#junto d1 y d2 y los ordeno
d3 = d1 + d2;
d3.sort()


#2)PREGUNTA: Manipular los datos
edad       = []
studytime  = []
cant       = 0
sum_edad   = 0
sum_study  = 0
absences = []


#Promedio de la edad y tiempo de estudio
for l in d3:
	linea = l.split(';')
	edad.append(int(linea[2]))
	studytime.append(int(linea[13]))
	absences.append(int(linea[29]))
	cant      = cant + 1
	sum_edad  = sum_edad  + int(linea[2])
	sum_study = sum_study + int(linea[13]) 


promedio_edad       = sum_edad/cant
promedio_time_study = sum_study/cant

print("PROMEDIO DE EDAD")
print(promedio_edad)
print("PROMEDIO DE TIEMPO DE ESTUDIO")
print(promedio_time_study)


#3) GRAFICAR HISTOGRAMA
pt.hist(edad,25, (15,22))
pt.xlabel('Edad')
pt.ylabel('Cantidad de Estudiantes')
pt.title('HISTOGRAMA SOBRE LA EDAD')
pt.show()

#4) GRAFICAR DIAGRAMA DE DISPERSION
pt.plot(absences)
pt.xlabel('Numero de Estudiantes')
pt.ylabel('Escuelas Cercanas')
pt.title('ESCUELAS ADYACENTES')
pt.show()






