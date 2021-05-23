import random
import time

tablero = [
             [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','',' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','═','═','═','═','═','═','═','═','═','═','═','═','═','═','═','═╣'],
             [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','║'],
             [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','║'],
             [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','║'],
             [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','║'],
             [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','║'],
             [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','║'],
             [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','║'],
             [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','║'],
             [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','║'],
             [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','║'],
             ['▄','▄','▄','▄','▄','▄', '▄','▄','▄','▄','▄','▄', '▄','▄','▄','▄','▄','▄', '▄','▄','▄','▄','▄','▄', '▄','▄','▄','▄','▄','▄', '▄','▄','▄','▄','▄','▄', '▄','▄', '║', '▄','▄','▄','▄','▄','▄', '▄']
             ]

palabras = ['arroz', 'boca', 'casa', 'dedo', 'elefante', 'foca', 'gato', 'hueco', 'imagen', 'jaula', 'kilo', 'limon', 'mosca', 'niño', 'opera', 'pera', 'queso', 'raton', 'salmon', 'tierra', 'uva', 'vaca', 'walle', 'xilofono', 'zapato']
palabras_jugadas = []

def imprime_tablero(tablero: list):
    for fila in tablero:
        for columna in fila:
            print(columna, end='')
        print('')
    print('\n'*2)

def palabra_aleatoria():
    while True:
        palabra = random.choice(palabras)
        print('escogi: ',palabra)
        if palabra not in palabras_jugadas:
            palabras_jugadas.append(palabra)
            return palabra

def imprime_palabras(palabra: list):
    print('\t'*2, end='')
    for letras in palabra:
        print(letras, end='')
    print('\n'*2)

def pide_letra(tablero_pistas: list):
    while True:
        letra_seleccionada = input('Ingrese una letra de la (a-z): ')
        if 'a' <= letra_seleccionada.lower() and 'z' >= letra_seleccionada.lower() and len(letra_seleccionada) == 1:
            if letra_seleccionada not in tablero_pistas:
                return letra_seleccionada
            else:
                print(f'\n\t........La letra "{letra_seleccionada}" ya fue seleccionada escoja otra....\n')
        else:
            print('\n\tERROR::::Escoja una letra de la "a" a la "z" no incluya la ñ\n')

def actualiza_pistas(letra:str, palabra_seleccionada: str, pistas):
    valor = False
    for posicion in range(len(palabra_seleccionada)):
        if palabra_seleccionada[posicion] == letra:
            pistas[posicion] = letra
            valor = True       
    return pistas, valor

def actualiza_tablero(tablero):
    if '|' not in tablero[2]:
        tablero[2][22]='|'
        tablero[3][22]='|'
        continuar_jugando = True
    elif '(' not in tablero[4]:
        tablero[4][21]='('
        tablero[4][22]='-_-'
        tablero[4][23]=')'
        tablero[4].pop(0)
        tablero[4].pop(25)
        continuar_jugando = True
    elif '|' not in tablero[5]:
        tablero[5][22]='|'
        tablero[6][22]='|'
        tablero[7][22]='|'
        continuar_jugando = True
    elif '/' not in tablero[6]:
        tablero[6][21]='/'
        tablero[7][20]='/'
        continuar_jugando = True
    elif '\ ' not in tablero[6]:
        tablero[6][23]='\ '
        tablero[7][24]='\ '
        tablero[6].pop(25)
        tablero[7].pop(25)
        continuar_jugando = True
    elif '|' not in tablero[8]:
        tablero[8][22]='|'
        tablero[9][22]='|'
        continuar_jugando = True
    elif '/' not in tablero[10]:
        tablero[10][21]='/'
        tablero[11][20]='/'
        continuar_jugando = True
    elif '\ ' not in tablero[10]:
        tablero[10][23]='\ '
        tablero[11][24]='\ '
        tablero[10].pop(25)
        tablero[11].pop(25)
        continuar_jugando = False
        print('\n\n:::::::::::::::::::::::::::::::::::Perdiste:::::::::::::::::::::::::::::::::::::::\n\n'.upper())
    return continuar_jugando

def inicio_juego(palabra_seleccionada, pistas, tablero):
    juega = True
    while juega:
        imprime_tablero(tablero)
        imprime_palabras(pistas)
        letra = pide_letra(pistas)
        pistas, retorno = actualiza_pistas(letra.lower(), palabra_seleccionada, pistas)
        if not retorno:
            juega = actualiza_tablero(tablero)
            if not juega:
                time.sleep(1)
                imprime_tablero(tablero)
                print('\t\tLa palabra era: ',palabra_seleccionada.title(),'\n' )
        elif '_ ' not in pistas:
            print('\n\t***************GANASTE**************\n')
            time.sleep(1)
            imprime_tablero(tablero)
            print('\t\tAcertaste¡ la palabra es: ',palabra_seleccionada.title(),'\n' )
            juega = False

def menu(pistas, tablero, palabra_seleccionada):
    menu = '''
                    
                    
                    
                    El siguiente es el juego del ahorcado 
                
                Seleccione una opción para empezar a jugar

                1. jugar
                2. cerrar
    '''.title()
    value = True
    while value:
        seleccion = input(menu+'\n\t-> ')
        if seleccion == '1':
            inicio_juego(palabra_seleccionada, pistas, tablero)
            while True:
                seguir = input('Desea Continuar si/no?: ')
                if seguir.lower() == 'si' or seguir.lower() == 's':
                    tablero = []
                    for lista in tablero_copy:
                        lista_copy = []
                        for espacio in lista:
                            lista_copy.append(espacio)
                        tablero.append(lista_copy)
                    pistas = pistas_copy[:]
                    palabra_seleccionada = palabra_aleatoria()
                    pistas = ['_ ']*len(palabra_seleccionada)
                    break
                elif seguir.lower() == 'no' or seguir.lower() == 'n':
                    time.sleep(1)
                    value = False
                    print('\n\t_____________ GRACIAS POR USAR ESTE JUEGO_____________\n')
                    break
                else:
                    time.sleep(0.2)
                    print('\n\t:::::ERROR::::Seleccione una opción del menú\n')
                    time.sleep(0.5)

        elif seleccion == '2':
            time.sleep(1)
            print('\n\t_____________ GRACIAS POR USAR ESTE JUEGO_____________\n')
            value = False
        else:
            time.sleep(0.2)
            print('\n\t:::::ERROR::::Seleccione una opción del menú\n')
            time.sleep(0.5)
            
palabra_seleccionada = palabra_aleatoria()

pistas = ['_ ']*len(palabra_seleccionada)
pistas_copy = pistas[:]
tablero_copy = []
for lista in tablero:
    lista_copy = []
    for espacio in lista:
        lista_copy.append(espacio)
    tablero_copy.append(lista_copy)

menu(pistas, tablero, palabra_seleccionada)


       


        
        






    



    



