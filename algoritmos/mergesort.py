def mergesort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left_arr = mergesort(arr[:middle])
    rigth_arr = mergesort(arr[middle:])
    return merge(left_arr, rigth_arr)


def merge(left_arr, rigth_arr):
    result = list()
    i = j = 0

    while i < len(left_arr) and j < len(rigth_arr):
        if left_arr[i] < rigth_arr[j]:
            result.append(left_arr[i])
            i += 1
        else:
            result.append(rigth_arr[j])
            j += 1

    while i < len(left_arr):
        result.append(left_arr[i])
        i += 1

    while j < len(rigth_arr):
        result.append(rigth_arr[j])
        j += 1

    return result


unordered_list = [4, 3, 2, 1, 9, 8, 7, 6, 5]
print(unordered_list)
ordered_list = mergesort(unordered_list)
print(ordered_list)
