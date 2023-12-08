
def quicksort(arr, left, right):
    if left < right:
        middle = partition(arr, left, right)
        quicksort(arr, left, middle)
        quicksort(arr, middle+1, right)


def partition(arr, left, right):
    pivot = arr[right-1]

    i = left - 1

    for j in range(left, right-1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    i += 1
    arr[i], arr[right-1] = arr[right-1], arr[i]
    return i


unordered_list = [4, 3, 2, 1, 9, 8, 7, 6, 5]
print(unordered_list)
quicksort(unordered_list, 0, len(unordered_list))
print(unordered_list)
