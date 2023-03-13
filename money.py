def money():
    monedas={"Peso":1,"Dolar":1,"Euro":1,"2Pesos":2,"5Dolares":5}
    print("Quieres agregar una moneda: (si/no)")
    ok=input()
    if ok=="si":
        x=input("Inserte Moneda: ")
        y=int(input("Inserte Valor Moneda: "))
        monedas.setdefault(x,y)
    else:
        None
    print("Estas son las monedas guardadas",monedas)
    print("Quiere trabajar con alguna moneda:(si/no) ")
    ok=input()
    if ok == "si":
        print("Que operacion quiere hacer: ")
        print("1 -  Suma\n 2 -  Resta\n 3 - Multiplicar \n 4 -  Dividir")
        yolo=input()
        if yolo == "1":
            x=input("Inserte Moneda: ")
            y=input("Inserte Otra Moneda: ")
            suma(monedas[x],monedas[y])
        elif yolo == "2":
            resta(monedas[x],monedas[y])
            x=input("Inserte Moneda: ")
            y=input("Inserte Otra Moneda: ")
        elif yolo == "3":
            x=input("Inserte Moneda:")
            y=int(input("Por Cuanto: "))
            Multiplicar(monedas[x],y)
        elif yolo == "4":
            x=input("Inserte Moneda:")
            y=int(input("Por Cuanto: "))
            Dividir(monedas[x],y)
        else:
            print("inserta un valor valido")
    else:
        print("Hasta Luego!!")


def suma(num1,num2):
    print("El resultado es: $",num1+num2)

def resta(num1,num2):
    print("El resultado es: $",num1-num2)

def Multiplicar(num1,num2):
    print("El resultado es: $",num1*num2)

def Dividir(num1,num2):
    print("El resultado es: $",num1/num2)

money()





#print(monedas["Peso"]+monedas["5Dolares"])



