def bubble_sort(input_array):
    
    for j in range(len(input_array), 0, -1):
        for i in range(len(input_array)-1):
            
            if input_array[i] > input_array[i + 1]:
                input_array[i], input_array[i + 1 ] = input_array[i + 1], input_array[i]
    return input_array


test_list = [1, 3, 2, 12, 4, 13, 12, 33, 2, 7, 6, 0]

print(bubble_sort(test_list))