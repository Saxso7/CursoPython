# por convencion de la comunidad python
# Al parametro con * se le llama args(tipo tupla)
def promedio(*args):
    return sum(args) / len(args)

resultado = promedio(6.5,6.2,6.3)
print(resultado)


def combinacion(p1, p2, *args, p4=1000):
    print(p1)
    print(p2)
    print(args)
    print(p4)

combinacion(10, 20, 1, 2, 3, 4, 5, 6, p4=1000)

#kwargs al llevar doble asterico se convierte en diccionario

def combinacion_dos(*args, **kwargs):
    print(args)
    print(kwargs)

combinacion_dos(1, 2, 3, 4, 5, seba=True, curso='Python')