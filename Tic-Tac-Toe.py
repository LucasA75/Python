#Tic Tac Toe para 2 Jugadores

print("Bienvenido al juego: Tic Tac Toe")

elTablero = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in elTablero:
    board_keys.append(key)



def Tabla(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():
    
    count = 0
    marca = input("Que marca quieres ser:(x/o) ")
    marca = marca.upper()
        
    for i in range(10):
        Tabla(elTablero)
        print("Es tu Turno," + marca + ".Donde quieres colocar?")

        move = input()        

        if elTablero[move] == ' ':
            elTablero[move] = marca
            count += 1
            if marca == "X":
                marca = "O"
            elif marca == "O":
                marca = "X"
        else:
            print("El lugar esta ocupado.\nDonde quieres colocar?")
            continue

         
        if count >= 5:
           
            if elTablero['7'] == elTablero['8'] == elTablero['9'] != ' ': 
                Tabla(elTablero)
                print("\nJuego Terminado.\n")
                if marca == "X":
                    marca = "O"
                elif marca == "O":
                    marca = "X"

                print(" **** " +marca + " gano. ****")                
                break
            elif elTablero['4'] == elTablero['5'] == elTablero['6'] != ' ':
                Tabla(elTablero)
                print("\nJuego Terminado.\n")  
                if marca == "X":
                    marca = "O"
                elif marca == "O":
                    marca = "X"              
                print(" **** " +marca + " gano. ****")
                break
            elif elTablero['1'] == elTablero['2'] == elTablero['3'] != ' ': 
                Tabla(elTablero)
                print("\nJuego Terminado.\n")   
                if marca == "X":
                    marca = "O"
                elif marca == "O":
                    marca = "X"             
                print(" **** " +marca + " gano. ****")
                break
            elif elTablero['1'] == elTablero['4'] == elTablero['7'] != ' ': 
                Tabla(elTablero)
                print("\nJuego Terminado.\n")
                if marca == "X":
                    marca = "O"
                elif marca == "O":
                    marca = "X"                
                print(" **** " +marca + " gano. ****")
                break
            elif elTablero['2'] == elTablero['5'] == elTablero['8'] != ' ': 
                Tabla(elTablero)
                print("\nJuego Terminado.\n")
                if marca == "X":
                    marca = "O"
                elif marca == "O":
                    marca = "X"                
                print(" **** " +marca + " Gano. ****")
                break
            elif elTablero['3'] == elTablero['6'] == elTablero['9'] != ' ': 
                Tabla(elTablero)
                print("\nJuego Terminado.\n")
                if marca == "X":
                    marca = "O"
                elif marca == "O":
                    marca = "X"                
                print(" **** " +marca + " Gano. ****")
                break 
            elif elTablero['7'] == elTablero['5'] == elTablero['3'] != ' ': 
                Tabla(elTablero)
                print("\nJuego Terminado.\n")
                if marca == "X":
                    marca = "O"
                elif marca == "O":
                    marca = "X"                
                print(" **** " +marca + " Gano. ****")
                break
            elif elTablero['1'] == elTablero['5'] == elTablero['9'] != ' ': 
                Tabla(elTablero)
                print("\nJuego Terminado.\n")
                if marca == "X":
                    marca = "O"
                elif marca == "O":
                    marca = "X"                
                print(" **** " +marca + " GANO. ****")
                break 

        if count == 9:
            print("\nJuego Terminado.\n")                
            print("Es un empate!!")    
    
    restart = input("Quieres jugar de nuevo?(si/no)")
    if restart == "si" or restart == "si":  
        for key in board_keys:
            elTablero[key] = " "

        game()
    else:
        print("Gracias por jugar")

if __name__ == "__main__":
    game()
