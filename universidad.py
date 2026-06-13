class universidad:
    def __init__(self, nombre: str, rector: str, año: int ):
        self.nombre = nombre
        self.rector = rector
        self. año = año

    def presentarse(self):
        return f"{self.nombre}, hola, soy{self.rector} fui creado{self.año}."

# probar lo que hice
if __name__ == " _main_ ":
    intep = universidad("intep","german colonia",1979)
    print(intep.presentarse())