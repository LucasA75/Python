#class Perro:
#    trucos = [] # uso incorrecto de una variable de clase
    
#    def __init__(self, nombre):
#        self.nombre = nombre
    
#    def agregar_truco(self, truco):
#         self.trucos.append(truco)

#d = Perro('Fido')
#e = Perro('Buddy')
#d.agregar_truco('girar')
#e.agregar_truco('hacerse el muerto')
#d.trucos # compartidos por todos los perros inesperadamente
 #['girar', 'hacerse el muerto']


#El diseño correcto de esta clase sería usando una variable de instancia:
class Perro:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.trucos = [] # crea una nueva lista vacía para cada perro
 
    def agregar_truco(self, truco):
        self.trucos.append(truco)

d = Perro('Fido')

e = Perro('Buddy')

d.agregar_truco('girar')

e.agregar_truco('hacerse el muerto')

d.trucos
['girar']

e.trucos
['hacerse el muerto']


class Mapeo:
    def __init__(self, iterable):
        self.lista_de_items = []
        self.__actualizar(iterable)
    def actualizar(self, iterable):
        for item in iterable:
            self.lista_de_items.append(item)
    __actualizar = actualizar # copia privada del actualizar() original
class SubClaseMapeo(Mapeo):
    def actualizar(self, keys, values):
        # provee una nueva signatura para actualizar()
        # pero no rompe __init__()
        for item in zip(keys, values):
            self.lista_de_items.append(item)




