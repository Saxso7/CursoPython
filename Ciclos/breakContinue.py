titulo = 'Curso profesional de Python'

for caracter in titulo:
    if caracter == 'P':
        break #break termina de manera inmediata el cliclo el ciclo
    print(caracter)



for caracter in titulo:
    if caracter == ' ':
        continue #continue hace un salto a la siguiente iteracion omitiendo el caracter
    print(caracter)