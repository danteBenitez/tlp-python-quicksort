def quicksort(number_list: list[int | float]) -> list[int | float]:
    """
        Utiliza el algoritmo de quicksort para ordenar una lista de números
        *in_place* (sin utilizar memoria adicional).

        :param number_list: lista de números a ordenar
        :type list[int | float]

        :return: lista de números ordenados
        :rtype: list[int | float]
    """
    # Aquí llamamos a la implementación de quicksort.
    # Lo realizamos de este modo para que consumidores de la función 
    # no deban preocuparse por colocar los índices correctos.
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
    length = end - start
    # Caso base:
    # Si el largo es menor o igual a 1, entonces la sublista ya está ordenada.
    # Retornar la lista como está.
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

assert quicksort([]) == []
assert quicksort([1]) == [1]
assert quicksort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert quicksort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
assert quicksort([5,4, 6, 8, 9, 1, 3, 10, -2, -4]) == [-4, -2, 1, 3, 4, 5, 6, 8, 9, 10]
assert quicksort([5, 3, 3, 2, 4, 1, 1]) == [1, 1, 2, 3, 3, 4, 5]
assert quicksort([-3, -1, -4, -1, -5, -9, -2, -6, -5, -3, -5]) == [-9, -6, -5, -5, -5, -4, -3, -3, -2, -1, -1]
assert quicksort([1000000, 999999, -1000000, -999999, 0]) == [-1000000, -999999, 0, 999999, 1000000]
assert quicksort([92, 27, 33, 48, 12, 55, 34, 91, 5, 87, 72, 58, 19, 47, 3, 50, 23, 62, 82, 41, 20, 38, 15, 31, 81, 16, 10, 13, 70, 45, 79, 64, 85, 2, 89, 77, 43, 69, 88, 26, 30, 35, 78, 63, 74, 73, 68, 1, 17, 46, 22, 21, 65, 25, 52, 39, 37, 60, 76, 32, 6, 42, 29, 4, 40, 83, 53, 54, 59, 71, 14, 66, 84, 67, 24, 51, 56, 36, 11, 86, 44, 28, 9, 75, 8, 7, 18, 49, 61, 57, 90, 80, 99, 100, 98, 97, 95, 96, 93, 94]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

print("¡Pruebas pasadas exitosamente!")
