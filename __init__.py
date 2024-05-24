def swap(arr, from_index, to_index):
    [arr[from_index], arr[to_index]] = [arr[to_index], arr[from_index]]
    return arr

def quicksort(number_list: list[int]) -> list[int]:
    return quicksort_impl(number_list, 0, len(number_list))

def quicksort_impl(number_list: list[int], start: int, end: int) -> list[int]:
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

    # print(number_list)
print(quicksort([1, 2, 3, 4, -10, -20]))
print(quicksort([5,4, 6, 8, 9, 1, 3, 10, -2, -4]))
# print(quicksort([0, 1, -1, 2]))
# quicksort([-10, -2, 10, 30, -5, -11])
