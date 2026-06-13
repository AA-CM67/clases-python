class Alumno:
    def __init__(self, nombre: str, edad: int, matricula: str):
       self.nombre = nombre
       self.edad = edad
       self.matricula = matricula 
    
    def presentarse(self):
        return f"Hola, soy {self.nombre}, mi edad {self.edad} año y mi matricua {self.matricula}."
    
    def clasificacion(self):
        if self.edad < 18:
            return "soy un alumno de menor de edad."
        elif self. edad < 28:
            return " soy  un alumno de mediana edad."
        elif self. edad < 60:
            return " soy un alumno adulto."
        
        else:
            return "soy un alumno universitario mayor de edad."
    
    #probar lo que hice
Alumno1 = Alumno("alejandra", 18,"263965")
print(Alumno1.presentarse(), Alumno1.clasificacion())

Alumno2 = Alumno("brayan",28,"92107")
print(Alumno2.presentarse(), Alumno2.clasificacion())

Alunmo3 = Alumno("leidy",36,"495278")
print(Alunmo3.presentarse(), Alunmo3.clasificacion())

Alumno4 = Alumno("jazz",65,"581239")
print(Alumno4.presentarse(), Alumno4.clasificacion) 
          