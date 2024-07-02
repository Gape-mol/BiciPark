# Importo las librerias necesarias, csv para el manejo de archivos y datetime para poder guardar y almacenar la hora de entrada y salida.
import csv
from datetime import datetime

# Clase Usuario para referenciar a las personas que vayan a ocupar el servicio.
class Usuario:
    def __init__(self, nombre, matricula, telefono):
        self.nombre = nombre
        self.matricula = matricula
        self.telefono = telefono
        # self.lugar = lugar # Esta variable es para proximamente añadir un objeto bicicleta e incluir lo que teniamos pensado de que al momento de registrar pida modelo de bicicleta y asi.

# Clase para registrar las horas de entrada y salida de un objeto usuario.
class Registro:
    def __init__(self, usuario, hora_entrada):
        self.usuario = usuario
        self.hora_entrada = hora_entrada
        self.hora_salida = None

# Clase para la gestión de archivos
class GestorArchivo:
  @staticmethod
  def guardar_datos(registros, filename):
    # Abro el archivo en modo escritura y añado los titulos de las columnas
    with open(filename, "w", newline="") as f:
      writer = csv.writer(f)
      writer.writerow(["Nombre", "Matricula", "Telefono", "Hora de Entrada", "Hora de Salida"])
      # Mediante un for recorro la lista de registros y añado los datos de cada registro
      for r in registros:
        writer.writerow([r.usuario.nombre, r.usuario.matricula, r.usuario.telefono, r.hora_entrada.strftime("%Y-%m-%d %H:%M:%S"), r.hora_salida.strftime("%Y-%m-%d %H:%M:%S") if r.hora_salida else None])
        print("Registros guardados con éxito.")

  @staticmethod
  def cargar_datos(filename):
    registros = []
    try:
      # Abro el archivo en modo lectura
      with open(filename, "r") as f:
        reader = csv.DictReader(f)
        # Recorro el archivo y añado los objetos usuario y registro guardados al diccionario y lista de la funcion principal
        for row in reader:
          usuario = Usuario(row["Nombre"], row["Matricula"], row["Telefono"])
          registro = Registro(usuario, datetime.strptime(row["Hora de Entrada"], "%Y-%m-%d %H:%M:%S"))
          if row["Hora de Salida"]:
            registro.hora_salida = datetime.strptime(row["Hora de Salida"], "%Y-%m-%d %H:%M:%S")
            registros.append(registro)
      print("Registros cargados con éxito.")
    except FileNotFoundError:
      print("El archivo no se ha podido encontrar.")
    return registros

# La clase principal que gestiona nuestro sistema
class BiciPark:
    def __init__(self, gestor_archivo):
      filename = "Registros.csv"
      self.usuarios = {}  # Utilizo un diccionario para guardar los objetos usuario, ya que necesito asociar una matricula al nombre, telefono, etc
      self.registros = gestor_archivo.cargar_datos(filename)  # Aca una lista para los registros, ya que solo quiero almacenar los objetos de registro.
      self.gestor_archivo = gestor_archivo

    # Función para registrar usuarios, conectando su nombre con su matricula y su numero de telefono.
    def registrar_usuario(self, nombre, matricula, telefono):
        # Aca compruebo si el numero de matricula esta registrado, porque aunque los nombres se pueden repetir la matricula es exclusiva al ir asociada al RUT
        if matricula in self.usuarios:
            print("El usuario ya se encuentra registrado.")
        # Si el usuario no existe, se crea y se añade a al diccionario de usuarios
        else:
            self.usuarios[matricula] = Usuario(nombre, matricula, telefono)
            print("El usuario ha sido registrado con éxito.")

    # Función para registrar la hora de entrada de un usuario.
    def registrar_entrada(self, matricula):
        # Compruebo si la matricula esta dentro del diccionario de usuarios y si el if se cumple, se añade a la lista de registros
        if matricula in self.usuarios:
            usuario = self.usuarios[matricula]
            registro = Registro(usuario, datetime.now())
            self.registros.append(registro)
            print(f"Entrada registrada para: {usuario.nombre}")
        else:
            # Si no se cumple, se muestra un mensaje de error
            print("Usuario no encontrado.")

    # Función para registrar la hora de salida de un usuario.
    def registrar_salida(self, matricula):
        # Compruebo si la matricula esta dentro del diccionario de usuarios, llendo valor por valor del diccionario y si el if se cumple, se revisa si la hora de salida esta vacia, en ese caso, se añade a la lista de registros
        for registro in self.registros:
            if registro.usuario.matricula == matricula and registro.hora_salida is None:
                registro.hora_salida = datetime.now()
                print(f"Salida registrada para: {registro.usuario.nombre}")
                return
        print("Registro de entrada no encontrado.")

    # Función para guardar los registros
    def guardar_registros(self):
      filename = "Registros.csv"
      self.gestor_archivo.guardar_datos(self.registros, filename)

    # Función para mostrar los registros existentes en pantalla
    def mostrar_registros(self):
        for registro in self.registros:
            salida = registro.hora_salida.strftime("%Y-%m-%d %H:%M:%S") if registro.hora_salida else "En uso"
            print(f"Usuario: {registro.usuario.nombre}, Matricula: {registro.usuario.matricula}, Entrada: {registro.hora_entrada.strftime('%Y-%m-%d %H:%M:%S')}, Salida: {salida}")

    # Función para buscar los datos de un usuario por su matricula, para ver su nombre, telefono, etc.
    def buscar_usuario(self, matricula):
        if matricula in self.usuarios:
            usuario = self.usuarios[matricula]
            print(f"Nombre: {usuario.nombre}, Matricula: {usuario.matricula}, Telefono: {usuario.telefono}")
        else:
            print("El usuario no se ha encontrado.")

# Función para salir
def salir():
    print("Cerrando el programa...")

# El menu de siempre
def menu():
    gestor_archivo = GestorArchivo()
    bici_park = BiciPark(gestor_archivo)

    while True:
        print("Menu de selección")
        print("1) Registrar usuario")
        print("2) Registrar entrada")
        print("3) Registrar salida")
        print("4) Mostrar registros")
        print("5) Guardar registros")
        print("6) Buscar usuario")
        print("7) Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre = input("Nombre: ")
            matricula = input("Matricula: ")
            telefono = input("Telefono: ")
            bici_park.registrar_usuario(nombre, matricula, telefono)
        elif opcion == "2":
            matricula = input("Matricula: ")
            bici_park.registrar_entrada(matricula)
        elif opcion == "3":
            matricula = input("Matricula: ")
            bici_park.registrar_salida(matricula)
        elif opcion == "4":
            bici_park.mostrar_registros()
        elif opcion == "5":
            bici_park.guardar_registros()
        elif opcion == "6":
            matricula = input("Matricula: ")
            bici_park.buscar_usuario(matricula)
        elif opcion == "7":
            salir()
            break
        else:
            print("Opción no válida, vuelva a intentarlo.")

# Ejecuto el menu desde el inicio del programa
menu()
