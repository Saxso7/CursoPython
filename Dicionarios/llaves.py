diccionario = {'a':1, 'b':2, 'c':3, 'd':4}

#Metodo Keys / obtener llaves (recomendable por seguridad tupla de llaves)
llaves = tuple(diccionario.keys())
print(llaves)

#Metodo values / obtener valores
valores = tuple(diccionario.values())
print(valores)

#Metodo items
elementos = tuple(diccionario.items())
print(elementos)