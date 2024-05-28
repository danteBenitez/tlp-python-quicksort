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
    return quicksort_impl(number_list, 0, len(number_list) - 1)

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
    # El largo de la sublista. Puesto que los límites son inclusivos, 
    # sumamos uno para obtener el largo real.
    length = end - start + 1
    # Caso base:
    # Si el largo es menor o igual a 1, entonces la sublista ya está ordenada.
    # Retornar la lista como está.
    if length <= 1:
        return number_list

    # Selección del pivote como el elemento medio de la sublista.
    pivot_index = start + (end - start) // 2
    pivot = number_list[pivot_index]

    # Partición: Reordenamos la sublista de modo que los valores menores al 
    # pivote se encuentren a la izquierda y los mayores a la derecha de un índice
    # dado por `pivot_index`. Lo que sigue es una implementación de la partición 
    # de Hoare, que tiene mejor complejidad algoritmica que sus alternativas.
    # Véase: https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme

    # Definimos dos índices, uno izquierdo y otro derecho.
    left = start - 1
    right = end + 1
    while True:
        # Avanzamos el índice izquierdo mientras encontremos valores
        # menores que el pivote.
        left += 1
        while number_list[left] < pivot:
            left += 1

        # Avanzamos el índice derecho mientras encontremos valores
        # mayores que el pivote. 
        right -= 1
        while number_list[right] > pivot:
            right -= 1

        # Si los índices se han cruzado, entonces el algoritmo ha terminado.
        if left >= right:
            # Para este punto, las siguientes condiciones se cumplen:
                # - a la derecha del índice `right` hay valores no menores al pivote
                #   (puesto que los que eran menores se han intercambiado)
                # - a la izquierda del índice `right` hay valores no mayores al pivote
                #    (puesto que los que eran mayores se han intercambiado)
            # Es decir, el índice `right` cumple con las condiciones de la partición
            # y podemos usarlo para continuar con el ordenamiento.
            pivot_index = right
            break
        
        # Si no, intercambiamos las posiciones de los elementos correspondientes.
        number_list[left], number_list[right] = number_list[right], number_list[left]

    # Caso recursivo: Llamamos a *quicksort_impl* para ordenar
    # las sublistas que formamos: 
        # - una sublista va desde start hasta pivot_index
        # - la otra va desde pivot_index + 1 hasta end
    quicksort_impl(number_list, start, pivot_index)
    quicksort_impl(number_list, pivot_index + 1, end)

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
