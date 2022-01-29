#           0  ,      1   ,   2  ,   3
lista = ['Python','Django','Ruby','Java']
lista_2 = ['PHP']

#agregar datos a las lista
#lista.append('PHP')

#agregar dato a la lista con un indice definido
lista.insert(0,'C++')

#agregamos datos de la segunda variable listas_2
lista.extend(lista_2)
print(lista) 


sub_lista = lista[0:3]
print(sub_lista) 


#removemos un dato de la lista
lista.remove('Ruby')

#removemos por indice con palabra reservada del
del lista[0]

#removemos todos los datos de una lista
lista.clear()

print(len(lista)) 
print(lista) 

# start:end
# start: -> obtenemos los ultimos elementos de la lista
# :end -> obtenemos los primeros elementos de la lista
# start:end:skip
