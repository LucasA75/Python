import random

print("Bienvenido a la tira de Dados")
x=str(input("ingrese si para tirar los dados o no para salir:  "))
if x =="si":
	while x == "si":
		result = random.choice([1, 2, 3, 4, 5, 6])
		result2= random.choice([1, 2, 3, 4, 5, 6])
		print("al tirar 1 dado se obtuvo :", result)
		print ("al tirar el 2 dado se obtuvo: ",result2)
		x=str(input("ingrese (si/no) para continuar: "))
		if x == "no":
			print("Gracias por jugar")
elif x =="no":
	print("Hasta luego!")