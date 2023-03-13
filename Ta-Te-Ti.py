import time
import random

# TABLERO INICIAL VACIO
tablero = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# LISTA CON LAS POSICIONES DISPONIBLES EN EL TABLERO
# OJO: NO SON LOS INDICES DE LA LISTA SINO LAS POSICIONES QUE EL USUARIO VE Y ELIGE 
disponibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# FUNCIONES REQUERIDAS
def imprimeTablero():
    print('   |   |')
    print(' ' + tablero[0] + ' | ' + tablero[1] + ' | ' + tablero[2])
    print('   |   |')
    print('___ ___ ___')
    print('   |   | ')
    print(' ' + tablero[3] + ' | ' + tablero[4] + ' | ' + tablero[5])
    print('   |   | ')
    print('___ ___ ___')
    print('   |   | ')
    print(' ' + tablero[6] + ' | ' + tablero[7] + ' | ' + tablero[8])
    print('   |   |')
    print('\n')

# Actualiza el tablero con los simbolos del jugador o de la mÃ¡quina en las posiciones elegidas
def actualizaTablero(posElegida, simbolo):
    tablero[posElegida - 1] = simbolo
    return tablero

# Elimina de la lista disponibles la posiciÃ³n que es seleccionada 
def actualizaDisponibles(numero):
    disponibles.remove(numero)
    return disponibles

# Verifica si el jugador o la mÃ¡quina ganaron, buscando en horizontal, vertical o diagonal, 3 simbolos en lÃ­nea 
def esGanador(simbolo):
    if( (tablero[0]==simbolo and tablero[1]==simbolo and tablero[2]==simbolo) or (tablero[3]==simbolo and tablero[4]==simbolo and tablero[5]==simbolo) or (tablero[6]==simbolo and tablero[7]==simbolo and tablero[8]==simbolo) or (tablero[0]==simbolo and tablero[3]==simbolo and tablero[6]==simbolo) or (tablero[1]==simbolo and tablero[4]==simbolo and tablero[7]==simbolo) or (tablero[2]==simbolo and tablero[5]==simbolo and tablero[8]==simbolo) or (tablero[0]==simbolo and tablero[4]==simbolo and tablero[8]==simbolo) or (tablero[2]==simbolo and tablero[4]==simbolo and tablero[6]==simbolo) ):
        return True
    else:
        return False

# Verifica si la posiciÃ³n elegida por el jugador ya no se encuentra en la lista disponibles, lo que significa que esa posiciÃ³n ya fuÃ© ocupada
def posicionOcupada(numero):
    if(numero not in disponibles):
        return True
    else:
        return False

# IMPRIMIMOS EL TABLERO VACIO ANTES DE COMENZAR
imprimeTablero()

# ELEGIMOS LOS SIMBOLOS CON LOS QUE JUGARÃN EL JUGADOR Y LA MÃQUINA
jugador1 = input("Jugador1 Deseas jugar con la 'X' o con la 'O' : ").upper()
jugador2 = ''
if(jugador1 == 'X'):
    print("Elegiste la 'X' tÃº inicias el juego")
    jugador2 = 'O'  
elif(jugador1 == 'O'):
        print("Elegiste la 'O' el Jugador2 comienza el juego")
        jugador2 = 'X'
        

# EL VALOR INICIAL DE LA VARIABLE juego ES True
juego = True

# INICIO DEL JUEGO, MIENTRAS EL VALOR DE juego SEA True EL JUEGO CONTINUARÃ
while(juego):
    
    #####   COMIENZA EL JUEGO EL JUGADOR1   #####
    if(jugador1 == 'X'):
        posElegida = int(input("Jugador1: Elije una posiciÃ³n entre el 1 y 9 : "))
        while(posicionOcupada(posElegida)):
            nuevaElegida = int(input("La posiciÃ³n que elegiste esta ocupada, elige otro nÃºmero: "))
            posElegida = nuevaElegida
        print('\n')
        
        tablero = actualizaTablero(posElegida, jugador1)
        disponibles = actualizaDisponibles(posElegida)
        imprimeTablero()
        if(esGanador(jugador1)):
            print("GANARON LAS X")
            break
        time.sleep(1)

        # CONTINUA EL TURNO DEL JUGADOR2
        if((len(disponibles) == 0) and not esGanador(jugador1)):
            print("FUE UN EMPATE!!!")
            break 
        # La mÃ¡quina elige al azar una posiciÃ³n que este disponible en la lista disponibles
        pos = int(input("Jugador2: Elije una posiciÃ³n entre el 1 y 9 : "))
        while(posicionOcupada(pos)):
            nuevaElegida = int(input("La posiciÃ³n que elegiste esta ocupada, elige otro nÃºmero: "))
            pos = nuevaElegida
        print('\n')
        
        tablero = actualizaTablero(pos, jugador2)
        disponibles = actualizaDisponibles(pos)
        imprimeTablero()
        if(esGanador(jugador2)):
            print("GANARON LAS O")
            break
        time.sleep(1)
        
    #####   COMIENZA EL JUEGO EL JUGADOR2   #####
    else:
        if(jugador2 == 'X'):
            # La mÃ¡quina elige al azar una posiciÃ³n que este disponible en la lista disponibles
            pos = int(input("Jugador2: Elije una posiciÃ³n entre el 1 y 9 : "))
            while(posicionOcupada(pos)):
                nuevaElegida = int(input("La posiciÃ³n que elegiste esta ocupada, elige otro nÃºmero: "))
                pos = nuevaElegida
            print('\n')
            
            tablero = actualizaTablero(pos, jugador2)
            disponibles = actualizaDisponibles(pos)
            imprimeTablero()
            if(esGanador(jugador2)):
                print("GANARON LAS X")
                break
            time.sleep(1)

            # CONTINUA EL TURNO DEL JUGADOR
            if((len(disponibles) == 0) and not esGanador(jugador2)):
                print("FUE UN EMPATE!!!")
                break

            posElegida = int(input("Jugador1 Elije una posiciÃ³n entre el 1 y 9 : "))
            while(posicionOcupada(posElegida)):
                nuevaElegida = int(input("La posiciÃ³n que elegiste esta ocupada, elige otro nÃºmero: "))
                posElegida = nuevaElegida
            print('\n')
            
            tablero = actualizaTablero(posElegida, jugador1)
            disponibles = actualizaDisponibles(posElegida)
            imprimeTablero()
            if(esGanador(jugador1)):
                print("GANARON LAS O")
                break
            time.sleep(1)

print("TerminÃ³ el juego")