#!/usr/bin/python3
"""def: matrix divided
    @matrix: 1 param
    @div: 2 param
    return new_matrix"""


def matrix_divided(matrix, div):
    """# creo una lista vacia que hara a que se importe el resultado"""
    new_matrix = []
    """div must be a number (integer or float)"""
    if div is None or type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    """condition division zero"""
    if div == 0:
        raise ZeroDivisionError("division by zero")

    prevlen = len(matrix[0])
    for row in matrix: 
        """Each row of the matrix must be of the same size"""
        if len(row) != prevlen:
            raise TypeError("Each row of the matrix must have the same size")
        for column in row:
            """matrix must be a list of lists of integers or floats"""
            if type(column) is not int and type(column) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        prevlen = len(row)

    """# recorro la lista del matrix"""
    for row in matrix:
        """# Crearemos un array vacio donde almacenara los array divididos"""
        div_matrix = []
        for column in row:
            """# agregara en el array"""
            div_matrix.append(round(column / div, 2))
        new_matrix.append(div_matrix)

    return new_matrix
