#cada elemento les corresponde un indice
#dentro de una tupla puedes almacenar todo tipo de datos incluyendo listas y tuplas
#una tupla es cuando usaremos datos usando siempre los mismos datos y estos no mutaran

#dentro de esta tiene indices
#          0         1    2      3         4                 5
tupla = ('String ', 10 , 15.4 , True , [1 , 2 , 3 ], ( 4 , 5 , 6))

print(tupla)
print(type(tupla) )


cursos = ('Python','Django','Ruby','Java')
primer_curso = cursos[0]
print(primer_curso)

# se pueden usar saltos
sub_tupla = cursos[:2]
print(sub_tupla)

#Funciones y listas
#para crear una lista con una tupla o viceversa

niveles = ['Basico','Intermedio','Avanzado']

cursos_lista = list(cursos)
print (cursos_lista)

niveles_tupla = tuple(niveles)
print (niveles_tupla)