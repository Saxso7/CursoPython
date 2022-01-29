#ejemplo 1
'''
contador = 1


# While se ejecuta hasta que la condicion deje de cumplirse
while contador <= 10:
    print(contador)
    contador = contador + 1
'''
#ejemplo 2
numero = 1234
contador = 0

#ciclo para contar la cantidad de numeros, de la variable numero
while numero >= 1:
    contador += 1
    #al restar por 10 vamor a restar un digito al numero
    numero = numero / 10
else:
    print('Fin de el ciclo while')
    print(contador)

