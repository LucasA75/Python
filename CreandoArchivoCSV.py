import csv
#a_list = ['Pedro','Florencia','Matias','Jorge','Maria','Ines']

#with open('d:/Python/a.csv', 'w') as csvfile:
 #   writer = csv.writer(csvfile)
 #   writer.writerow(a_list)

reader = csv.reader(['Hola;,Mundo','Python'],escapechar=';')
file_content = list(reader)
print(file_content)

#Esta es la respuesta correcta! Al definir 
# el lector indicamos que el carácter ;
# va a escapar los caracteres especiales 
# como el delimitador, el quotechar, etc. 
# Por eso la coma dentro del primer campo 
# (fila uno, columna uno) se leyó como ‘Hola, Mundo’ 
# y no como dos columnas, la primera con el contenido
#  ‘Hola’ y la segunda con el contenido ‘Mundo’

