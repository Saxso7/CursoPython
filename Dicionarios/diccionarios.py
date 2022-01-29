#variable para diccionario, el juego de llaves dice que un diccionario

elementos = {'a':1, 'b':2, 'c':3, 'd':4}
'''
#para añadir un valor asignamos la [ llave ] = valor de la llave 

elementos['nombre'] = 'Sebastian'#Crea la llave

elementos['nombre'] = 'Mulan'#Actualiza valor de la llave
'''
#obtener un valor
valor = elementos['d']

#obtener valor con metodo get/ llave, mensaje en caso que valor no exita
resultado = elementos.get('z','llave no existe')

#obtener valor con metodo setdefault

resultado2 = elementos.setdefault('z',20)

print(valor)
print(elementos)
print(len(elementos))
print(resultado)
print(resultado2)

#para condicionar un valor se puede usar la palabra reservada IN
print ('x' in elementos)

#si las llaves estan duplicadas, esta añade solo uno