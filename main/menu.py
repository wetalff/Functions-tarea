import models.classes as c
import dao.Functions as f

estudiantes = f.EstudianteDao()


def menu():
    print(""" 
          1. Agregar 
          2. Mostrar 
          6. Salir 
          Digite una opcion:
        """)
          
          
def main():
    while(True):
        menu()
        option = input()
        if option == '1':
            nombre = input("Nombre del estudiante: ")
            apellido = input("Apellido: ")
            carrera = input("Carrera: ")
            año = int(input("Año: "))
            promedio = float(input("promedio: "))
            estudiante = c.Product(nombre, apellido, carrera, año, promedio)
            estudiantes.add(estudiante) 
        elif option == '2':
            print("Estudiantes")
            estudiantes.show()
        elif option == '6':
            print('Adios')
            False
            break
        else:
            print('Opcion invalida')