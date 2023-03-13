#string="Hola Mundo Python!"
#print("\"Hola \n Mundo!\"")
#a_list = ["1","2","3"]
#"{}-{}-{}".format(a_list) #tampoco funciona
#x= "-".join(a_list)
#print(x)
nro_cuenta="32673"
saldo=100.2543
print("El saldo de la cuenta {} es ${:.2f}".format(nro_cuenta,saldo))
#esta bien , pero tmb se puede
print("El saldo de la cuenta {:s} es ${:.2f}".format(nro_cuenta,saldo))
