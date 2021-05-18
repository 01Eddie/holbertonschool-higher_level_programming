#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):    
    # declarar e inicializar el contador
    counter = 0
    # declara variable auxiliar para imprimir la linea de elementos
    line = ""
    # iterar los elementos del array con la variable i en el rango de x
    for i in range(x):
        # si el contador < x
        if counter < x: # 0 < 2 x -- lo compara al valor introducido en la funcion
            try:
                # imprimir el elemento i del array my_list
                print("{:d}".format(my_list[i]), end="")
                # aumentamos counter en 1
                counter += 1
                # ValueError: Se genera cuando una operación o función recibe un argumento que tiene el tipo correcto pero un valor inapropiado
                # TypeError: Se genera cuando se aplica una operación o función a un objeto de tipo inadecuado. El valor asociado es una cadena que proporciona detalles sobre la falta de coincidencia de tipos.
            except (ValueError, TypeError):
                continue
    print()
    return counter