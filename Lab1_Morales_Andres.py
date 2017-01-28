
import csv, operator


with open("C://student-mat.csv") as csvarchivo:
	entrada = csv.reader(csvarchivo)
	for reg in entrada:
        print(reg)  # Cada línea se muestra como una lista de campos
	


