# Find a key value in the given integer array.
# The array must be sorted ascending.
def binary_search(array, key):
    li = 0
    re = len(array) - 1
    while re >= li:
        m = int((li + re) / 2)
        if key == array[m]:
            return m
        if key < array[m]:
            re = m - 1
        else:
            li = m + 1
    return -1


input_array = [0, 2, 3, 4, 5, 7, 8, 10, 11]
search_key = 5
found_index = binary_search(input_array, search_key)
print("binary_search(", input_array, ",", search_key, ") =>", found_index)
