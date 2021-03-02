'''
Condition 1 : The list only has distinct elements, and elements are in a strictly increasing order.
Conditino 2 : Return the index of value, or -1 if the value doesn't exist in the list.
'''


def binary_search(input_array, value):

    low = 0
    high = len(input_array)-1

    while low <= high: 

        mid = int((low + high) / 2)
        
        if input_array[mid] == value:
            return mid

        elif input_array[mid] < value:
            low = mid + 1

        else:
            high = mid - 1

    return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25  # -1 # this value doesn't exist in the list
test_val2 = 15  # 4
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)



"""
def binary_search(input_array, value):

    original = input_array

    while len(input_array) >= 1:

        idx = round(len(input_array)/2)-1

        if len(input_array) == 1 and input_array[idx] == value:
            return original.index(input_array[idx])

        elif input_array[idx] > value:
            input_array = input_array[:idx]

        elif input_array[idx] < value:
            input_array = input_array[idx+1:]

    return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25  # -1 # this value doesn't exist in the list
test_val2 = 15  # 4
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
"""