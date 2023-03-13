demo_list = [1, "hello", 1.34, True, [1, 2, 3]]
colors = ["red", "green", "blue"]

numbers_list = list((1, 2, 3, 4))
#se puede ocupar una tupla para que funcione

#print(type(numbers_list))
#r = list(range(1, 10))
#print(r) 
#de donde a donde quiero crear una lista
#range llega hasta 1 numero antes del ultimo numero

#print(len(colors))
# con la funcion dir puedo obtener un directorio de funciones
#print(colors [1])
#los [] se ocupa para saber que esta en esa posicion
#print("green" in colors)
# in = en obvio ( da como valor True o False)
#print(colors)
#colors[1] = "yellow" # para cambiar un valor en una lista
#print(colors)
#print(dir(colors))
#colors.append("violet", "yellow")
#para agregar un solo valor
#colors.extend(["violet", "yellow"])
#para agregar mas de 1 solo valor
#se deben ocupar tuplas

colors.insert(1, "violet")
#insert se ocupa para insertar en un lugar especifico
colors.insert(len(colors),"yellow")
#print(colors)
#append = agregar

#colors.pop() # borrar segun el indice , si se deja () borra last
#colors.pop()
colors.remove("green")
# borrar un valor especifico
#colors.clear()
#borra todo
colors.sort() #ordena alfabeticamente
# reverse= True para ordenar alrevez
#count , sirve para contar cuantas veces un valor se repite
print(colors)

