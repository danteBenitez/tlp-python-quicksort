def quicksort(number_list: list[int | float]) -> list[int | float]:
    """
        Utiliza el algoritmo de quicksort para ordenar una lista de números
        *in_place* (sin utilizar memoria adicional).

        :param number_list: lista de números a ordenar
        :type list[int | float]

        :return: lista de números ordenados
        :rtype: list[int | float]
    """
    return quicksort_impl(number_list, 0, len(number_list))

def quicksort_impl(number_list: list[int | float], start: int, end: int) -> list[int | float]:
    """
        Implementación recursiva del algoritmo de quicksort
        que ordena una sublista de `number_list` dado un rango
        de índices [start, end). El ordenamiento es *in_place*.

        :param number_list: lista de números a ordenar
        :type list[int | float]

        :param start: índice de inicio de la sublista
        :type int

        :param end: índice de fin de la sublista
        :type int
    """
    length = end - start + 1
    if length <= 1:
        return number_list
    
    pivot_index = start
    pivot = number_list[pivot_index]
    i = start + 1
    while i < end:
        number = number_list[i]
        if number <= pivot:
            number_list.pop(i)
            number_list.insert(pivot_index, number)
            pivot_index += 1
        else:
            number_list.pop(i)
            number_list.insert(pivot_index + 1, number)
        i += 1

    quicksort_impl(number_list, start, pivot_index)
    quicksort_impl(number_list, pivot_index+1, end)
    return number_list

assert quicksort([1, 2, 3, 4, -10, -20]) == [-20, -10, 1, 2, 3, 4]
assert quicksort([5,4, 6, 8, 9, 1, 3, 10, -2, -4] == [-4, -2, 1, 3, 4, 5, 6, 8, 9, 10])
assert quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5] 

print("¡Pruebas pasadas exitosamente!")
