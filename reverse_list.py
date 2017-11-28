"""
Exercício que retorna uma lista com os elementos invertidos
"""


def reverse_list(lista):
    """
    Reverses order of elements in list l.
    """
    return lista[::-1]


def reverse_list_2(lista):
    """
    Another way
    """
    return [i for i in reversed(lista)]
