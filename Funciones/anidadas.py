# dentro de una funcion, puede existur una funcion anidada
def operacion(cantidad, balance, tipo=1):


    def deposito(cantidad, balance):
        return cantidad + balance


    def retiro(cantidad, balance):
        if cantidad <= balance:
            return balance - cantidad
        else:
            print('Monto insuficiente')
            return None
        
    if tipo == 1:
        return deposito(cantidad, balance)
    elif tipo == 2:
        return retiro(cantidad, balance)
    

resultado = operacion(100000, 234400, 2)
print(resultado)
