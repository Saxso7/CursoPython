titulo_curso = 'Curso profesional de Python'

contador = titulo_curso.count('Python')

print(contador)


print('python' in titulo_curso.lower())

#para saber si un string esta al inicio  se usa starswith()
print(titulo_curso.startswith('Curso'))

#para saber si esta al final
print(titulo_curso.endswith('Python'))