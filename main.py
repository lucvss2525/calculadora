#calculadora#
from funciones import suma, resta, multiplicacion, division

print("""
    ------
    suma 1
    -------
    resta 2
    -------
    multiplicacion 3
    ----------------
    division 4
    ----------
    """)

M = int(input('ingrese una opcion :'))

if M == 1:
    print ('Ud eligio  suma')
    A = int (input('Ingrese Numero 1: '))
    B = int (input('Ingrese Numero 2: '))
    suma(A,B)
elif M == 3:
    print ('Ud eligio  multiplicacion')
    A = int (input('Ingrese Numero 1: '))
    B = int (input('Ingrese Numero 2: '))
    multiplicacion(A,B)
elif M == 4:
    print ('Ud eligio  division')
    A = int (input('Ingrese Numero 1: '))
    B = int (input('Ingrese Numero 2: '))
    division(A,B) 
