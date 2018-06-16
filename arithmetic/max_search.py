def max_element(array):
    j = 0
    i = 0
    x = array[j]
    while i < len(array):
        if array[i] > x:
            j = i
            x = array[i]
        i += 1
    return j


input_array = [1, 5, 33, 2, 34, 2, 7]
max_index = max_element(input_array)
print("max_element(", input_array, "):", max_index, "=>", input_array[max_index])
