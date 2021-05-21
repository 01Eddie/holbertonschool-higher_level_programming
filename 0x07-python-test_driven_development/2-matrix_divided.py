#!/usr/bin/python3

def matrix_divided(matrix, div):
    # creo una lista vacia que hara a que se importe el resultado
    new_matrix = []
    # recorro la lista del matrix
    for x in matrix:
        # Crearemos un array vacio donde almacenara los array divididos
        div_matrix = []
        for y in x:
            # agregara en el array
            div_matrix.append(round(y / div, 2))

        new_matrix.append(div_matrix)
    #if new_matrix is list: 
    return new_matrix