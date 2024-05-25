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
    # El largo de la sublista a ordenar. 
    length = end - start + 1
    # Caso base:
    # Si el largo es menor o igual a 1, entonces la sublista ya está ordenada
    # retornar la lista como está.
    if length <= 1:
        return number_list

    # Selección del pivote como el primer elemento de la sublista.
    pivot_index = start
    pivot = number_list[pivot_index]

    # Partición: Reordenamos la lista de modo que los números menores
    # al pivote estén a la izquierda y los mayores a la derecha.
    # Como el pivote es el primer elemento, comenzamos la partición desde
    # el segundo elemento de la sublista
    i = start + 1

    # Mientras que no hayamos avanzado hasta el final...
    while i < end:
        # Tomamos un número de la sublista
        number = number_list[i]
        # Si es menor o igual al pivote...
        if number <= pivot:
            # Lo insertamos a la izquierda, es decir...
            # ...lo removemos de su posición original...
            number_list.pop(i)
            # ...y lo insertamos justo antes de la posición del pivote
            number_list.insert(pivot_index, number)

            # Luego de la inserción, la posición del pivote
            # aumenta en uno
            pivot_index += 1
        else:
            # Si el elemento es mayor al pivote, lo insertamos a la derecha...
            # ... lo removemos de su posición original...
            number_list.pop(i)
            # ... lo insertamos justo después de la posición del pivote.
            number_list.insert(pivot_index + 1, number)

            # Colocar un elemento a la derecha no cambia la posición 
            # del pivote.
        i += 1

    # Caso recursivo: Llamamos a *quicksort_impl* para ordenar
    # las sublistas que formamos: 
        # - una sublista va desde start hasta pivot_index
        # - la otra va desde pivot_index + 1 hasta end
    quicksort_impl(number_list, start, pivot_index)
    quicksort_impl(number_list, pivot_index+1, end)

    # Finalizamos la recursión retornando la lista luego de que haya sido
    # modificado por las anteriores llamadas
    return number_list

assert quicksort([1, 2, 3, 4, -10, -20]) == [-20, -10, 1, 2, 3, 4]
assert quicksort([5,4, 6, 8, 9, 1, 3, 10, -2, -4]) == [-4, -2, 1, 3, 4, 5, 6, 8, 9, 10]
assert quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5] 

print("¡Pruebas pasadas exitosamente!")
