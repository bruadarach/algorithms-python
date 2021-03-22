def quicksort(array):

    array_len = len(array)
    if (array_len <= 1):
        return array
    else:
        pivot = array[0]
        greater = [i for i in array[1:] if i > pivot]
        lesser = [i for i in array[1:] if i <= pivot]
        return quicksort(lesser) + [pivot] + quicksort(greater)


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
