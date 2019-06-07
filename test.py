from unittest import TestCase
from Movimientos_damas_chinas import *
from test1 import *

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
        dado = [tablero,5,3,4,2]
        espero = [tablerop]
        obtengo = mover_pieza(dado)
        self.assertEquals(espero, obtengo)

    def test_mover_pieza(self):
        dado = [tablerop,2,4,3,3]
        espero = [tablerop1]
        obtengo = mover_pieza(dado)
        self.assertEquals(espero, obtengo)

    def test_mover_pieza(self):
        dado = [tablerop2,4,2,2,4]
        espero = [tablerop3]
        obtengo = mover_pieza(dado)
        self.assertEquals(espero, obtengo)

    def test_mover_pieza(self):
        dado = [tablerop3,2,4,0,2]
        espero = "camino bloqueado"
        obtengo = mover_pieza(dado)
        self.assertEquals(espero, obtengo)

    def test_cambiar_pieza(self):
        dado = [tablerop4,2,7,0,5]
        espero = [tablerop5]
        obtengo = mover_pieza(dado)
        self.assertEquals(espero, obtengo)

    def test_mover_reina(self):
        dado = [tablerop5,0,5,0,5]
        espero = [tablerop6]
        obtengo = mover_pieza(dado)
        self.assertEquals(espero, obtengo)
