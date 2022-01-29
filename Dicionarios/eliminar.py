diccionario = {'a':1, 'b':2, 'c':3, 'd':4}

print(len(diccionario))
#palabra reservada del + diccionario['llave']
del diccionario['d']
print(diccionario)

#metodo pop / retorna el valor de la llave antes de borrar
valor = diccionario.pop('c')
print(valor)

#para eliminar todo
diccionario.clear()
print(diccionario)

print(len(diccionario))