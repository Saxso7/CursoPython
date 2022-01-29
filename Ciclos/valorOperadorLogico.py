# Python toma como valor, el primer valor booleano, no es limitado a solo String
variable = 'Sebastian' or 'CodigoFacilito'
variable2 = '' or 0 or [] or {} or () or True

print(variable, variable2)

listado = []
nombre = 'Sebastian'

'''
#La condicion con solo poner una variable, si esta es false no cumplira la condicion
#listado es False
if listado:
    resultado = listado
else:
    resultado = nombre
    '''

resultado = listado or nombre

print(resultado)
