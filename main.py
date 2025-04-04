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
elif M == 2:
    print ('Ud eligio  suma')
    A = int (input('Ingrese Numero 1: '))
    B = int (input('Ingrese Numero 2: '))
    resta(A,B)
    