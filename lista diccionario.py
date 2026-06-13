# Lista de diccionarios
personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 30, "ciudad": "Bogotá"},
    {"nombre": "Carlos", "edad": 22, "ciudad": "Lima"},
    {"nombre": "aleja","edad":18, "ciudad": "cali"},
    {"nombre": "sebas","edad": 39,"ciudad": "barcelona"}
]

# Mostrar en vertical
for persona in personas:
    print("nombre:", persona["nombre"])
    print("edad:", persona["edad"])
    print("ciudad:", persona["ciudad"])
    print("-------------------")