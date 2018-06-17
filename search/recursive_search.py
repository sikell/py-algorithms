def recursive_search(array, key):
    return search(array, 0, len(array) - 1, key)


def search(array, li, re, key):
    if (re - li) < 0:
        return -1
    m = int((li + re) / 2)
    if key == array[m]:
        return m
    if key < array[m]:
        return search(array, li, m - 1, key)
    else:
        return search(array, m + 1, re, key)


input_array = [0, 2, 3, 4, 5, 7, 8, 10, 11]
search_key = 5
found_index = recursive_search(input_array, search_key)
print("recursive_search(", input_array, ",", search_key, ") =>", found_index)


search_key = 11
found_index = recursive_search(input_array, search_key)
print("recursive_search(", input_array, ",", search_key, ") =>", found_index)


search_key = 0
found_index = recursive_search(input_array, search_key)
print("recursive_search(", input_array, ",", search_key, ") =>", found_index)
