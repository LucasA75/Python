#Juego del Gato

print("Bienvenido al Juego del Ta Te Ti")
hello=str(input("Quieres jugar contra la IA o contra otra persona:(IA/2)"))


#IA
if hello == "IA":
    print("No se Hacer inteligencia artificial, xd")
#Dos jugadores
elif hello== "2":
    player=input("Elegir Marca Primer Jugador:(x/o)")
    if player == "x":
        player ="x"
        player2 ="o"
        player
    
    elif player =="o":
        player ="o"
        player2 ="x"
    
    else:
        print("Elige una marca Valida....gil")
        player = False

    if player == True:
        print("Jugador elegir casilla")
        print("|  1  |  2  |  3   | \n_________________\n|  4  |  5   |  6   | \n_________________\n|  7  |  8  |  9   |  ")    
        y=input("Elige del 1 al 9")
        if y == "1":
            a1=player
            b1=""
            c1=""
            print('|  {}  |  {}  |   {}  |'.format(a1,b1,c1))
        elif y =="2":
            b1=player
            a1=""
            c1=""
            print('|  {}  |  {}  |   {}  |'.format(a1,b1,c1))
        elif y == "3":
            c1=player
            a1=""
            b1=""
            print('|  {}  |  {}  |   {}  |'.format(a1,b1,c1))


def Tablero(tab):
    print('|'+ tab[1]  +  '|'+  tab[2]  + '|'+  tab[3] + '|')
    print(" __________________")
    print("")
    print('|'+ tab[4]  +  '|'+  tab[5]  + '|' + tab[6] + '|')
    print(" __________________")
    print("")
    print('|'+ tab[7]  +  '|' + tab[8]  + '|'  +tab[9] + '|')

