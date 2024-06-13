import datetime
from datetime import datetime
import csv

"""
#Clase encargada de la Gestion de archivos
class gestor_archivo():
    filename = "Cicloparqueaderos.csv"
    #Funcion de guardado de datos
    @staticmethod
    def guardar_datos(bicicletas, filename):
        with open(filename, "w", newline='') as data:
            csv_writer = csv.writer(data) #Crea un objeto csv writer que sera el encargado de escribir nuestro csv
            csv_writer.writerow(["Marca", "Modelo", "Color", "Matricula", "Hora"]) #El objeto escribe en la primera fila los titulos de las columnas
    #Funcion de carga de datos
    @staticmethod
    def cargar_datos(bicicletas, filename):
        with open(filename, mode='r') as data:
            csv_reader = csv.DictReader(data)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f"Los nombres de cada columna son: {", ".join(row)}")
                    line_count += 1
                print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
                line_count += 1
            print(f'Processed {line_count} lines.')

gestor_archivo.guardar_datos
"""

marca = "bmx"
modelo = "Todoterreno"
color = "Negra con azul"
numero = 101
nombre = "John"
matricula = 21111222324
c = datetime.now()
hora_actual = c.strftime("%H:%M:%S")
fecha_actual = c.strftime("%d/%m/%Y")
print(f"La bicicleta se ha recivido a las {hora_actual} el dia: {fecha_actual}")

