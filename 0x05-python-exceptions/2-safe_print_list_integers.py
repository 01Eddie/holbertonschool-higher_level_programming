#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    # declarar e inicializar el contador
    counter = 0
    # declara variable auxiliar para imprimir la linea de elementos
    line = ""
    # iterar los elementos del array con la variable i en el rango de x
    for i in range(x):

        # si el contador<x
        if counter < x:
            try:
                print("{:d}".format(my_list[i]), end="")
                counter += 1
            except (ValueError, TypeError):
                continue
    print()
    return counter
