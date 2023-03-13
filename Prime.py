class Complejo:
    def __init__(self, partereal, parteimaginaria):
        self.r = partereal
        self.i = parteimaginaria

x = Complejo(3.0, -4.5)
print(x.r, x.i)

#Nota la importancia de ocupar self...aun nose k significa