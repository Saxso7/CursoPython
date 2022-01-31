# Para una funcion se usa la palabra reservada def
def suma(numero_uno, numero_dos):
    return numero_uno + numero_dos

numero_uno = int(input('Ingrese el primer numero: '))
numero_dos = int(input('Ingrese el segundo numero: '))
#para llamar una funcion
resultado = suma(numero_uno, numero_dos)
print('El resultado: ', resultado)

