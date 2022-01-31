#funcion calcular el area de un circulo
# podemos definir valor por default pi=3.14
def area_circulo(radio, pi=3.14):
    # EL VALOR POR DEFAULT SIEMPRE POR DERECHA
    return pi * (radio ** 2)

resultado = area_circulo(10)
print(resultado)