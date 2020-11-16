import random               # Importo la librería random 

# Inicia el programa con un "mini-menú"

print("""Bienvenido al Simulador de Dados 2020 by Siegfried Tomás
    ¿Desea iniciar el programa?
    1) Sí
    2) No""")
a = 0
a = input()
a = int(a)

# Si el valor es 1: el programa empieza y vuelve a preguntar si desea tirar nuevamente los dados.
# Si el valor es 2: el programa no se ejecuta.

if a == 1:
    while(True):

        dado1 = random.randint(1,6)             # Se definen ambas variables con la función "randint" entre el valor 1 y 6 
        dado2 = random.randint(1,6)

        print('--------------------------------------------------')
        print('El primer dado gira y su resultado es = ', dado1)
        print('El segundo dado gira y su resultado es = ', dado2)
        print('La suma de los dados es:', dado1 + dado2)
        print("""¿Quiere volver a tirar los dados?    
        1) Sí
        2) No""")
        print('--------------------------------------------------')

        b = input()
        b = int(b)

        if b == 1:          #Si el valor es 1: El programa vuelve a tirar los dados. | Si el valor es 2: El programa termina.
            a = 1
        elif b == 2:
            print("""Entendido, hasta luego...
            Fin del programa.""")
            break
        else:
            print("Por favor, vuelva a inicializar el programa e ingrese algún número de la lista...")
            break

elif a == 2:

    print("""Entendido, hasta luego...
    Fin del programa.""")

else:
    print("Por favor, vuelva a inicializar el programa e ingrese algún número válido de la lista.")
    


