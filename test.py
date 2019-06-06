from unittest import TestCase
from Movimientos_damas_chinas import *


tablero = [
        [' ', 'p', ' ', 'p', ' ', 'p', ' ', 'p'],
        ['p', ' ', 'p', ' ', 'p', ' ', 'p', ' '],
        [' ', 'p', ' ', 'p', ' ', 'p', ' ', 'p'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', 'P', ' ', ' ', ' ', ' ', ' ', ' '],
        ['P', ' ', ' ', ' ', 'P', ' ', 'P', ' '],
        [' ', 'P', ' ', 'P', ' ', 'P', ' ', 'P'],
        ['P', ' ', 'P', ' ', 'P', ' ', 'P', ' ']
    ]

tablero_secundario = [
        [' ', 'p', ' ', 'p', ' ', 'p', ' ', 'p'],
        ['p', ' ', 'p', ' ', 'p', ' ', 'p', ' '],
        [' ', 'p', ' ', 'p', ' ', 'p', ' ', 'p'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['P', ' ', 'P', ' ', 'P', ' ', 'P', ' '],
        [' ', 'P', ' ', 'P', ' ', 'P', ' ', 'P'],
        ['P', ' ', 'P', ' ', 'P', ' ', 'P', ' ']
    ]

tableropieza = [
        [' ', 'p', ' ', 'p', ' ', 'p', ' ', 'p'],
        ['p', ' ', 'p', ' ', 'p', ' ', 'p', ' '],
        [' ', 'p', ' ', 'p', ' ', 'p', ' ', 'p'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['P', ' ', 'P', ' ', 'P', ' ', 'P', ' '],
        [' ', 'P', ' ', 'P', ' ', 'P', ' ', 'P'],
        ['P', ' ', 'P', ' ', 'P', ' ', 'P', ' ']
    ]

    #tableros peón

#movimiento inicial
tablerop = [
        [' ', 'p', ' ', 'p', ' ', 'p', ' ', 'p'],
        ['p', ' ', 'p', ' ', 'p', ' ', 'p', ' '],
        [' ', 'p', ' ', 'p', ' ', 'p', ' ', 'p'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', 'P', ' ', ' ', ' ', ' ', ' ', ' '],
        ['P', ' ', ' ', ' ', 'P', ' ', 'P', ' '],
        [' ', 'P', ' ', 'P', ' ', 'P', ' ', 'P'],
        ['P', ' ', 'P', ' ', 'P', ' ', 'P', ' ']
    ]

#movimiento inicial del otro equipo
tablerop1 =[
        [' ', 'p', ' ', 'p', ' ', 'p', ' ', 'p'],
        ['p', ' ', 'p', ' ', 'p', ' ', 'p', ' '],
        [' ', 'p', ' ', ' ', ' ', 'p', ' ', 'p'],
        [' ', ' ', 'p', ' ', ' ', ' ', ' ', ' '],
        [' ', 'P', ' ', ' ', ' ', ' ', ' ', ' '],
        ['P', ' ', ' ', ' ', 'P', ' ', 'P', ' '],
        [' ', 'P', ' ', 'P', ' ', 'P', ' ', 'P'],
        ['P', ' ', 'P', ' ', 'P', ' ', 'P', ' ']
    ]

#tablero inicial comer pieza
tablerop2 = [
        [' ', 'p', ' ', 'p', ' ', 'p', ' ', 'p'],
        ['p', ' ', 'p', ' ', 'p', ' ', 'p', ' '],
        [' ', 'p', ' ', ' ', ' ', 'p', ' ', 'p'],
        [' ', ' ', 'p', ' ', ' ', ' ', ' ', ' '],
        [' ', 'P', ' ', ' ', ' ', ' ', ' ', ' '],
        ['P', ' ', ' ', ' ', 'P', ' ', 'P', ' '],
        [' ', 'P', ' ', 'P', ' ', 'P', ' ', 'P'],
        ['P', ' ', 'P', ' ', 'P', ' ', 'P', ' ']
    ]

#tablero final comer pieza y tablero de camino bloqueado por una pieza
tablerop3 = [
        [' ', 'p', ' ', 'p', ' ', 'p', ' ', 'p'],
        ['p', ' ', 'p', ' ', 'p', ' ', 'p', ' '],
        [' ', 'p', ' ', 'P', ' ', 'p', ' ', 'p'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['P', ' ', ' ', ' ', 'P', ' ', 'P', ' '],
        [' ', 'P', ' ', 'P', ' ', 'P', ' ', 'P'],
        ['P', ' ', 'P', ' ', 'P', ' ', 'P', ' ']
    ]

#Tablero inicial doblar por pieza reina
tablerop4 = [
        [' ', 'p', ' ', 'p', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', 'p', ' ', 'p', ' '],
        [' ', ' ', ' ', 'p', ' ', 'p', ' ', 'P'],
        ['p', ' ', 'p', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'P'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', 'P', ' ', 'P', ' ', ' ', ' ', 'P'],
        ['P', ' ', 'P', ' ', 'P', ' ', 'P', ' ']
    ]

#Tablero final cambiar pieza por pieza Reina e inicial de comer por Reina
tablerop5 = [
        [' ', 'p', ' ', 'p', ' ', 'R', ' ', ' '],
        [' ', ' ', ' ', ' ', 'p', ' ', ' ', ' '],
        [' ', ' ', ' ', 'p', ' ', 'p', ' ', ' '],
        ['p', ' ', 'p', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'P'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', 'P', ' ', 'P', ' ', ' ', ' ', 'P'],
        ['P', ' ', 'P', ' ', 'P', ' ', 'P', ' ']
    ]

# Tablero final comer por reina
tablerop6 = [
        [' ', 'p', ' ', 'p', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', 'p', ' ', ' '],
        ['p', ' ', 'R', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 'p', ' ', ' ', ' ', 'P'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', 'P', ' ', 'P', ' ', ' ', ' ', 'P'],
        ['P', ' ', 'P', ' ', 'P', ' ', 'P', ' ']
    ]


class Test_movimientos(TestCase):

    def test_tablero_a_cadena(self):
        dado = [tablero]
        espero = [tablero]
        obtengo = tablero_a_cadena(dado)
        self.assertEquals(espero, obtengo)

    def test_obtener_nombre_pieza(self):
        dado = "p"
        espero = "pieza blanca"
        obtengo = obtener_nombre_pieza(dado)
        self.assertEquals(espero, obtengo)


        #pruebas unitarias de la pieza

    def test_mover_pieza(self):
        dado = [tablero,1,1,3,1]
        espero = [tablerop]
        obtengo = mover_pieza(dado)
        self.assertEquals(espero, obtengo)

    def test_mover_pieza(self):
        dado = [tablerop,1,4,2,4]
        espero = [tablerop1]
        obtengo = mover_pieza(dado)
        self.assertEquals(espero, obtengo)

    def test_mover_pieza(self):
        dado = [tablerop2,4,1,3,2]
        espero = [tablerop3]
        obtengo = mover_pieza(dado)
        self.assertEquals(espero, obtengo)

    def test_mover_pieza(self):
        dado = [tablerop3,7,3,7.4]
        espero = "camino bloqueado"
        obtengo = mover_pieza(dado)
        self.assertEquals(espero, obtengo)

    def test_cambiar_pieza(self):
        dado = [tablerop4,"Q"]
        espero = [tablerop5]
        obtengo = mover_pieza(dado)
        self.assertEquals(espero, obtengo)
