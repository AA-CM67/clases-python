# lista de 6 frutas
frutas = ["mango", "papaya", "fresa", "melon", "uva", "banano"]

# agregar una fruta mas
frutas.append("naranja")

#mostrar todas las frutas usando for
print("lista de frutas con posicion:")

for i in range(len(frutas)):
    print(i, "-", frutas[i])
#seleccionar una fruta cambiando el numero
numero = 2   # cambia este numero para elegir otra fruta 

 # seleccionar una fruta especifica
print("\nfruta seleccionada:") 
print(frutas[numero])