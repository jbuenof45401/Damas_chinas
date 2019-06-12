from unittest import TestCase
from Movimientos_damas_chinas import *
from test1 import *

class Test_movimientos(TestCase):


    def test_obtener_nombre_peon(self):
        dado = "p"
        espero = "peon blancas"
        obtengo = obtener_nombre_peon(dado)
        self.assertEquals(espero, obtengo)


        #pruebas unitarias de la peon

    def test_mover_peon(self):
        dado = [tablero,5,2,4,1]
        espero = tablerop
        obtengo = mover_peon(tablero,5,2,4,1)
        self.assertEquals(espero, obtengo)

    def test_mover_peon(self):
        dado = [tablerop,2,4,3,3]
        espero = tablerop1
        obtengo = mover_peon(tablerop,2,4,3,3)
        self.assertEqual(espero, obtengo)

    def test_mover_peon(self):
        dado = [tablerop2,4,2,2,4]
        espero = tablerop3
        obtengo = mover_peon(tablerop2,4,2,2,4)
        self.assertEqual(espero, obtengo)

    def test_mover_peon(self):
        dado = [tablerop3,2,4,0,2]
        espero = "camino bloqueado"
        self.assertRaises(TypeError,mover_peon,tablerop3,2,4,0,2)




