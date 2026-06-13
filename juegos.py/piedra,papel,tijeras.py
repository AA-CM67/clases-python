import random

opciones = ["piedra", "papel", "tijeras"]

print("=== PIEDRA, PAPEL O TIJERAS ===")

seguir = "s"

while seguir == "s":
    jugador = input("Elige piedra, papel o tijeras: ").lower()

    while jugador not in opciones:
        print("Opción no válida. intenta de nuevo.")
        jugador = input("Elige piedra, papel o tijeras: ").lower()
        
    computadora = random.choice(opciones)

    print("La computadora eligió:", computadora)

    if jugador == computadora:
        print("¡Empate! Se juega otra ronda.")
        continue

    elif (
        (jugador == "piedra" and computadora == "tijeras") or
        (jugador == "papel" and computadora == "piedra") or
        (jugador == "tijeras" and computadora == "papel")
    ):
        print("¡Ganaste la partida!")

    else:
        print("¡La computadora ganó la partida!")
        seguir = input("¿desea seguir jugando? (s/n): ").lower()
        continue
        print("gracias por jugar.")
        
    