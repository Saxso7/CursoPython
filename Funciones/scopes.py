#Scope
animal = 'Leon' #Variable global -> funcion, ciclo o condicion

def imprimir_animal():
    global animal#con esto podemos usar o cambiar el valor de la variable global
    animal = 'Ballena' # Variable Local

    print(animal)
    print(id(animal))

imprimir_animal()

print(animal)
print(id(animal))