arr_1 = [10, 8, 11, 15, 5]
arr_2 = [1, 8, 11, 15]


def find_smallest(arr):
    smallest = arr[0]  # initially we take first element as smallest just for example
    smallest_index = 0  # here we just hold an index
    for i in range(1, len(arr)):
        if arr[i] < smallest:  # aar1 - 10 !< 10, then we take 8. 8 is lower -> smallest = 8, index = i = 1, same with 5
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    new_arr = []  # hold a new array
    for i in range(len(arr)):
        smallest = find_smallest(arr)  # find the smallest number in input array
        new_arr.append(arr.pop(smallest))  # remove this smallest number from input array and add to new empty array
                                           # then this process repeats, but there is another smallest number, since
                                           # previous was deleted
    return new_arr


print(selection_sort(arr_1))
