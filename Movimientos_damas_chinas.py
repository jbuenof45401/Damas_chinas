#PENDIENTES:
# 1. Pruebas
# 2. Regla de matar consecutivamente
# 3. Movimientos de Reinas

tablero = [
[' ', 'p', ' ', 'p', ' ', 'p', ' ', 'p'],
['p', ' ', 'p', ' ', 'p', ' ', 'p', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', 'P', ' ', 'P', ' ', 'P', ' ', 'P'],
['P', ' ', 'P', ' ', 'P', ' ', 'P', ' ']
]

def tablero_a_cadena(tablero):
    """
    (list of str) -> str
    recibimos un tablero o diccionario y devolvemos una cadena
    :param tablero: el tablero con la posicionde cada pieza
    :return: dict el tablero con la nueva posicion de las piezas
    """

    cadena = ""
    for fila in tablero:
        cadena += str(fila) + "\n"
    return cadena

def obtener_nombre_pieza(simbolo):
    """
    (str) -> str
    >>> obtener_nombre_pieza('p')
    'pieza piezas blancas'
    >>> obtener_nombre_pieza('P')
    'pieza Fiches Negras'
    Retorna el nombre de la pieza del ajedrez dado su simbolo
    :param simbolo: la representacion de la pieza segun el enunciado
    :return: El nombre y color de la pieza
    """
    tipo = 'Negras'
    if simbolo.islower():
        tipo = 'blancas'
    retorno = simbolo.lower()
    if retorno == 'p':
        return 'pieza '+tipo
    if retorno == 'r':
        return 'Reina '+tipo
    else:
        return 'No es una pieza'

def mover_pieza(tablero, x_inicial, y_inicial, x_final, y_final):
    '''
    ([][],int,int,int,int)-> [][]: tablero resultante del movimiento de un pieza.
    :param tablero: [][]: matriz con la posicion de las piezas
    :param x_inicial: int: entero indicando posicion en x inicial
    :param y_inicial: int: entero indicando posicion en y inicial
    :param x_final: int: entero indicando posicion en x final
    :param y_final: int: entero indicando posicion en y final
    :return: [][] tablero resultante
    '''

    if (0 <= x_final <= 7) and (0 <= y_final <= 7):
        esPeon = tablero[x_inicial][y_inicial] in 'pP'

        deltaX = abs(x_final - x_inicial)
        deltaY = abs(y_final - y_inicial)
        pieza = tablero[x_inicial][y_inicial]
        color_pieza = tablero[x_inicial][y_inicial].islower()

        if (esPeon):
            if (color_pieza == True):
                if (x_final > x_inicial):
                    if (deltaY == deltaX) and ((x_final != x_inicial) and (y_final != y_inicial)):
                        if ((deltaX == 1) and (deltaY == 1)):
                            if tablero[x_final][y_final] == ' ':
                                tablero[x_final][y_final] = pieza
                                tablero[x_inicial][y_inicial] = ' '

                                print( tablero_a_cadena(tablero) )
                            else:
                                print("La posicion final esta ocupada")
                        elif ((deltaX == 2) and (deltaY == 2)):
                            # Matar hacia la izquierda
                            if (y_final < y_inicial):
                                pieza_a_comer = tablero[x_final - 1][y_final + 1]
                                color_pieza_a_comer = pieza_a_comer.islower()
                                if (pieza_a_comer != ' ') and (color_pieza != color_pieza_a_comer):
                                    tablero[x_final - 1][y_final + 1] = ' '
                                    tablero[x_final][y_final] = pieza
                                    tablero[x_inicial][y_inicial] = ' '

                                    print( tablero_a_cadena(tablero) )
                                else:
                                    print("Movimiento invalido: no se puede mover 2 posiciones sin comer pieza enemiga")
                            # Matar hacia la derecha
                            elif (y_final > y_inicial):
                                pieza_a_comer = tablero[x_final - 1][y_final - 1]
                                color_pieza_a_comer = pieza_a_comer.islower()
                                if (pieza_a_comer != ' ') and (color_pieza != color_pieza_a_comer):
                                    tablero[x_final - 1][y_final - 1] = ' '
                                    tablero[x_final][y_final] = pieza
                                    tablero[x_inicial][y_inicial] = ' '

                                    print( tablero_a_cadena(tablero) )
                                    # TODO
                                    # reclamar_reina(x_final, y_final)


                                else:
                                    print("Movimiento invalido: no se puede mover 2 posiciones sin comer pieza enemiga")

                        else:
                            print("Movimiento invalido: solo se puede avanzar 1 posicion, o 2 posiciones si se va a comer una pieza")
                    else:
                        print("Movimiento invalido: solo se puede mover en diagonal")
                else:
                    print("La pieza solo se mueve hacia adelante")
            if (color_pieza == False):
                if (x_final < x_inicial):
                    if (deltaY == deltaX) and ((x_final != x_inicial) and (y_final != y_inicial)):
                        if ((deltaX == 1) and (deltaY == 1)):
                            if tablero[x_final][y_final] == ' ':
                                tablero[x_final][y_final] = pieza
                                tablero[x_inicial][y_inicial] = ' '

                                print( tablero_a_cadena(tablero) )
                            else:
                                print("La posicion final esta ocupada")
                        elif ((deltaX == 2) and (deltaY == 2)):
                            # Matar hacia la izquierda
                            if (y_final > y_inicial):
                                pieza_a_comer = tablero[x_final - 1][y_final - 1]
                                color_pieza_a_comer = pieza_a_comer.isupper()
                                if (pieza_a_comer != ' ') and (color_pieza != color_pieza_a_comer):
                                    tablero[x_final - 1][y_final - 1] = ' '
                                    tablero[x_final][y_final] = pieza
                                    tablero[x_inicial][y_inicial] = ' '

                                    print( tablero_a_cadena(tablero) )
                                else:
                                    print("Movimiento invalido: no se puede mover 2 posiciones sin comer pieza enemiga")
                            # Matar hacia la derecha
                            elif (y_final < y_inicial):
                                pieza_a_comer = tablero[x_final - 1][y_final + 1]
                                color_pieza_a_comer = pieza_a_comer.isupper()
                                if (pieza_a_comer != ' ') and (color_pieza != color_pieza_a_comer):
                                    tablero[x_final - 1][y_final + 1] = ' '
                                    tablero[x_final][y_final] = pieza
                                    tablero[x_inicial][y_inicial] = ' '

                                    print( tablero_a_cadena(tablero) )
                                    # TODO
                                    # reclamar_reina(x_final, y_final)


                                else:
                                    print("Movimiento invalido: no se puede mover 2 posiciones sin comer pieza enemiga")

                        else:
                            print("Movimiento invalido: solo se puede avanzar 1 posicion, o 2 posiciones si se va a comer una pieza")
                    else:
                        print("Movimiento invalido: solo se puede mover en diagonal")
                else:
                    print("La pieza solo se mueve hacia adelante")
            else:
                print('Posición final fuera del tablero.')

        return tablero


def mover_peonDiego(tablero, x_inicial, y_inicial, x_final, y_final):
    esPeon = tablero[x_inicial][y_inicial] in 'pP'
    ficha = tablero[x_inicial][y_inicial];
    posFinal = tablero[x_final][y_final];
    print(ficha)
    print(posFinal)
    #validación de movimiento y coordenadas válidas
    if ((0 <= x_final <= 7) and (0 <= y_final <= 7)) and ((0 <= x_inicial <= 7) and (0 <= y_inicial <= 7)) and ((x_inicial+1==x_final and y_inicial+1==y_final and ficha=='p') or (x_inicial-1==x_final and y_inicial+1==y_final and ficha=='p') or (x_inicial-1==x_final and y_inicial-1==y_final and ficha=='P') or (x_inicial+1==x_final and y_inicial-1==y_final and ficha=='P')):
        if esPeon:
            if posFinal == ' ':
                print("Peon " + ficha + " salta de la posición x: " + str(x_inicial) + " y: " + str(y_inicial) + " a la posición x: " + str(x_final) + " y: " + str(y_final))
                tablero[x_inicial][y_inicial] = " "
                tablero[x_final][y_final] = ficha
            elif posFinal in ficha:
                print("No se puede saltar fichas del mismo color")
            elif posFinal in 'pP':
                print("INCOMPLETO programar lógica de salto de ficha de diferente color")
    else:
        print("Movimiento no valido o coordenadas fuera del tablero")
    return tablero

print(tablero_a_cadena(tablero))
mover_peonDiego(tablero, 1,0,2,1)
print(tablero_a_cadena(tablero))

