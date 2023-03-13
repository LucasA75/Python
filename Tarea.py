import random
print("Favor ingrese Y para lanzar los dados, sino cualquier tecla para salir")
lee = input()
if lee == "y":
    while lee == "y":
        dados = random.choices([1,2,3,4,5,6], k=2)
        z = dados[0] + dados[1] 
        print("la suma de los dados es", z)
        print("Desea seguir lanzando?, presione Y por si, sino para salir presione cualquier tecla")
        lee = input()
        if lee != "y":
            print("ud. elijio salir, gracias")
            break
        else: 
            lee == "y"
else:
    print("Ud. elijio salir, gracias")