numeros = (1,2,3,4,5,6,7,8,9,10)

# * -> lista
# _ -> omitir

'''#Al asignar un *, python le asigna automaticamente el resto de valores de la tupla
uno, dos, tres, cuatro, *resto_valores = numeros'''

#Para omitir los valores se usa _, posteriormente se pueden usar los valores finales
uno, _, tres, cuatro, *_, nueve, diez = numeros


#al asignar a las variables la tupla numeros esta automaticamente define sus valores por indice
#esto se le llama descomprimir
print(uno) 
print(tres)
print(cuatro)
print(nueve)
print(diez)




