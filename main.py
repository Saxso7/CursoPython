from audioop import mul
import calculadora

nombre_completo = input('Ingrese su nombre completo: ')
edad = int(input('Ingrese su edad: '))
persona1 = calculadora.persona(nombre_completo,edad)
numero1 = int(input('Ingrese un numero: '))
numero2 = int(input('Ingrese el numero a elevar: '))
calculadora.multplicar_elevado(numero1,numero2)
