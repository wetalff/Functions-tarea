class Product:
    def __init__(self, name, apellido, carrera, año, promedio):
        self.name = name
        self.apellido = apellido
        self.carrera = carrera
        self.año = año
        self.promedio = promedio
        
        
    def __str__(self):
        return f"Nombre: {self.name} \nApellido: {self.apellido} \nCarerra: {self.carrera} \nAño: {self.año} \nPromedio: {self.promedio}"
    