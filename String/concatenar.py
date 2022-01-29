nombre = 'Sebastian Alexis'
apellido = 'Quezada'

#para concatenar se usa el operador +
nombre_completo = nombre + ' ' + apellido
print(nombre_completo)

nombre_completo2 = 'Sr. %s %s' %(nombre,apellido)
print(nombre_completo2)

#al igual que el anterior se puede usar placeholder
nombre_completo3 = 'Sr {} {} '.format(nombre,apellido)
print(nombre_completo3)

#Fstring para trabajar con interpolacion
nombre_completo4 = f'Sr. {nombre} {apellido} {"Cerda"}'
print(nombre_completo4)