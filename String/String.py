'''
lenguaje = 'Python Ruby Java Rust C++ C'
#la variable lenguaje, la convertimos en tipo lista con el metodo split
listado_lenguaje = lenguaje.split()
print(listado_lenguaje)
'''

#automaticamente los separa por los espacios, si queremos por otro caracter va dentro del parentesis ('-')
lenguaje = 'Python-Ruby-Java-Rust-C++-C'
#la variable lenguaje, la convertimos en tipo lista con el metodo split
listado_lenguaje = lenguaje.split('-',3)
print(listado_lenguaje )

lista = ['Python','Django','Ruby','Java']

lista_string = ' '.join(lista)
print(lista_string)