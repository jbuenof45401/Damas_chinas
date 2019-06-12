import math as m
from  test1 import *

#PENDIENTES:
# 1. Pruebas
# 2. Regla de matar consecutivamente
# 3. Movimientos de Reinas

tablero = [
[' ', 'p', ' ', 'p', ' ', 'p', ' ', 'p'],
['p', ' ', 'p', ' ', 'p', ' ', 'p', ' '],
[' ', 'P', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', 'P', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', 'P', ' ', 'P', ' ', 'P'],
['P', ' ', ' ', ' ', 'P', ' ', 'P', ' ']
]

def tablero_a_cadena(tablero):
    """
    (list of str) -> str
    recibimos un tablero o diccionario y devolvemos una cadena
    :param tablero: el tablero con la posicionde cada peon
    :return: dict el tablero con la nueva posicion de las peons
    """

    cadena = ""
    for fila in tablero:
        cadena += str(fila) + "\n"
    return cadena

def obtener_nombre_peon(simbolo):
    """
    (str) -> str
    >>> obtener_nombre_peon('p')
    'peon blancas'

    >>> obtener_nombre_peon('P')
    'peon Negras'

    Retorna el nombre de la peon del ajedrez dado su simbolo
    :param simbolo: la representacion de la peon segun el enunciado
    :return: El nombre y color de la peon
    """
    tipo = 'Negras'
    if simbolo.islower():
        tipo = 'blancas'
    retorno = simbolo.lower()
    if retorno == 'p':
        return 'peon '+tipo
    if retorno == 'r':
        return 'Reina '+tipo
    else:
        return 'No es una peon'

def equipoFicha(ficha):
    '''
    (str)->bool:blanca:False,Negra True

    >>> equipoFicha('p')
    False

    >>> equipoFicha('P')
    True


    :param ficha: str: la ficha a ser evaluada
    :return: bool: Blanca:False,Negra:True
    '''
    if(ficha in 'pPrR'):
        return ficha.isupper()
    else:
        raise TypeError("la ficha no es valida")

def mover_peon(tablero, x_inicial, y_inicial, x_final, y_final):
    tablero_resultante = tablero
    esPeon = tablero[x_inicial][y_inicial] in 'pP'
    esReina = tablero[x_inicial][y_inicial] in 'rR'
    ficha = tablero[x_inicial][y_inicial]
    posFinal = tablero[x_final][y_final]
    equipo = equipoFicha(ficha)
    if equipo:
        sentido_x = x_inicial-x_final
        sentido_y = y_inicial-y_final
    else:
        sentido_x = x_final-x_inicial
        sentido_y = y_final - y_inicial

    debecomer = False
    if(sentido_x>=2 or sentido_x<=-2) and (sentido_y<=-2 or sentido_y>=2):
        debecomer = True

    absolute_sent=m.sqrt(sentido_x**2)
    print(int(absolute_sent)%2)
    if int(absolute_sent)!=1:
        if int(absolute_sent)%2!=0:
            raise TypeError("Movimiento invalido")


    if  not esPeon and not esReina:
        raise Exception("Ficha invalida")

    #validación de movimiento y coordenadas válidas
    if((0 <= x_final <= 7) and (0 <= y_final <= 7)) and ((0 <= x_inicial <= 7) and (0 <= y_inicial <= 7)):
        if (x_inicial+sentido_x ==x_final and y_inicial + sentido_y==y_final):
                if posFinal == ' ':
                    print("Peon " + ficha + " salta de la posición x: " + str(x_inicial) + " y: " + str(y_inicial) + " a la posición x: " + str(x_final) + " y: " + str(y_final))
                    tablero_resultante[x_inicial][y_inicial] = ' '
                    tablero_resultante[x_final][y_final] = ficha
                    if equipo:
                        if(x_final==0):
                            tablero_resultante[x_final][y_final]="R"

                    else:
                        if(x_final==7):
                            tablero_resultante[x_final][y_final] = "r"


                    if debecomer:
                        sb = absolute_sent+1
                        for i in range(int(sb)):
                            if i ==0:
                                continue
                            if(sentido_x>0 and sentido_y>0):
                                comer_ficha = tablero_resultante[x_final-(i)][y_final-(i)]
                                tablero_resultante[x_final-(i)][y_final-(i)] = ' '
                            elif (sentido_x>0 and sentido_y<0):
                                comer_ficha = tablero_resultante[x_final-(i)][y_final-(i)]
                                tablero_resultante[x_final-(i)][y_final+(i)] = ' '
                            elif (sentido_x<0 and sentido_y<0):
                                comer_ficha = tablero_resultante[x_final-(i)][y_final-(i)]
                                tablero_resultante[x_final+i][y_final+i] = ' '
                            elif sentido_x<0 and sentido_y>0:
                                comer_ficha = tablero_resultante[x_final-(i)][y_final-(i)]
                                tablero_resultante[x_final+(i)][sentido_y-i] = ' '

                else:
                    raise Exception("No se puede saltar donde hay fichas")

    else:
        raise Exception("Movimiento invalido!")

    return tablero_resultante
mover_peon(tablero, 1,0,5,4)

