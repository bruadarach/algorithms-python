def linear_search(input_array, value):
    
    index = 0
    
    while input_array[index] != value:
        if index < len(input_array) and (input_array[index] < value):
            index += 1
        elif index > len(input_array) or input_array[index] != value:
            return -1
    return index


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25  # -1 # this value doesn't exist in the list
test_val2 = 15  # 4
print(linear_search(test_list, test_val1))
print(linear_search(test_list, test_val2))

