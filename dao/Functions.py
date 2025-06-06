#Data Access Object

""" Agregar productos """
""" Create
    Read
    Update
    Delete """

class EstudianteDao:
    def __init__(self):
        self.estudiantes = []
        
    
    def add (self,estudiante):
        self.estudiantes.append(estudiante)
        
        
    def show(self):
        for estudiante in self.estudiantes:
            print(estudiante)
            
        