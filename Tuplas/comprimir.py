#el resto de valores sera omitido ya que la combinacion debe ser exacta
lista = [1,2,3,4,5,6,7]
lista2 = [100,200,300,400,500]
tupla = (10, 20, 30, 40, 50)

resultado = zip(lista,tupla,lista2) # -> zip el orden va como ingremos la posicion de la lista o tupla
resultado = tuple(resultado)

print(resultado)
print(resultado[0][2])