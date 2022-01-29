def multplicar_elevado(numero1,numero2):
    elevado = numero1**numero2
    print('El resultado es: ',elevado)

def sumar(numero_sumar_1,numero_sumar_2):
    suma = numero_sumar_1 + numero_sumar_2
    print(suma)


class persona:
    def __init__(self,nombre_completo,edad):
        self.nombre = nombre_completo        
        self.edad = edad
        print('Bienvenido: ',nombre_completo,',Edad: ',edad)

class cliente:
    def __init__(self,rut_cliente):
        self.rut_cliente = rut_cliente        


