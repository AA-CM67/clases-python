class Alumno:
    def __init__(self, nombre: str, edad: int, matricula: str):
        self.nombre = nombre
        self.edad = edad
        self.matricula = matricula
  
    def describir(self) -> str:
        return  f"Hola, soy {self.nombre}, tengo {self.edad} año y mi matricula es {self.matricula}."
        
# bloque de prueba(se ejecuta solo al correo el archivo directamente)
if __name__ == "__main__":
    hector = Alumno("Hector Benavides",58,"79756893")
    print(hector.describir())