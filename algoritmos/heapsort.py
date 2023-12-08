def heapsort(arr):
    for i in range(len(arr)//2, -1, -1):
        downheap(arr, i, len(arr))

    for i in range(len(arr)-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        downheap(arr, 0, i)


def downheap(arr, i, heap_size):
    left_child = 2*i+1
    right_child = 2*i+2

    if left_child < heap_size:
        big_child = left_child
        if right_child < heap_size:
            if arr[right_child] > arr[left_child]:
                big_child = right_child
        if arr[big_child] > arr[i]:
            arr[i], arr[big_child] = arr[big_child], arr[i]
            downheap(arr, big_child, heap_size)


unordered_list = [4, 3, 2, 1, 9, 8, 7, 6, 5]
print(unordered_list)
heapsort(unordered_list)
print(unordered_list)
