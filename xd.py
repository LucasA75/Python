import time
class Semaforo(object):
    
    def __init__(self,color1,color2,color3):
        self.color1= color1 
        self.color2 = color2
        self.color3 = color3
    
    def tiempo(self):
        time.sleep(5)

    def col(self):
        
        luz = ("  ---- \n| {} | \n  ----")
        count = 0
        #Estructura
        while True:
            count += 1
            print(luz.format(self.color1))
            time.sleep(4)
            print(luz.format(self.color2))
            time.sleep(4)
            print(luz.format(self.color3))
            time.sleep(4)


x = Semaforo("Rojo","Amarillo","Verde")

x.col()


    
