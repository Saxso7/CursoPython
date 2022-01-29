from audioop import reverse


lista = [8,90,44,1,3,600]

#para ver el indice de un valor se usa el metodo index 
index = lista.index(90)
print('El numero de indice es el: ', index)

#para ordenar listas de un solo tipo de valor se usa sort, por defecto es acedente 
lista.sort()


#para mostrar el numero menor y el numero mayor se puede de la siguiente forma

print(lista)
'''
print(lista[0])#min
print(lista[-1])#max'''

#tambien existen metodos para traer los valores minimos y maximos
print(min(lista))#min
print(max(lista))#max

#en caso de que sea decendente 

lista.sort(reverse=True)


print(lista)

#en listas string me devuelve la con mas caracteres como minimo

lista2 = ['hola','como estas','Atte Sebastian Quezada']

lista2.sort()
print(max(lista2))

#para ver si se encuentra un valor dentro de la lista, al agreegar not niega el alor booleano
print(11 not in lista)


