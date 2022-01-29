calificacion = 7

#Ternario, creamos condicion en una linea de codigo
color = 'Verde' if calificacion >= 4 else 'Rojo'
'''
Esto seria lo normal
color = None

if calificacion >= 4:
    color = 'Verde'
else:
    color = 'Rojo'
'''

print(calificacion, color)