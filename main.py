from clases.enemigo import Enemigo
from clases.jugador import Jugador
import random

def main():
    nombre_jugador = input('Bienvenido, elegi un nombre')
    jugador = Jugador(nombre_jugador)

    enemigos = [
        Enemigo('Alien', 50, 10),
        Enemigo('Robot', 30, 5),
        Enemigo('Mounstro', 70, 15)
    ]

    print('Empieza la aventura')

    while True:
        enemigo_actual = random.choice(enemigos)
        print(f'Te enfrentas contra {enemigo_actual.nombre}en tu camino')

        while enemigo_actual.salud > 0:
            accion = input('¿Que deseas hacer? (atacar/huir)').lower()

            if accion == 'atacar':
                dano_jugador = jugador.atacar()
                print(f'Has atacado al {enemigo_actual.nombre} y le has causado {dano_jugador} de daño')