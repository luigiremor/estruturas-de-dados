def is_valid(utility, weight, disponibility):
    return utility > 0 and weight > 0 and disponibility > 0


def get_data():
    data = []
    index = 0
    while True:
        utility, weight, disponibility = map(int, input().strip().split(" "))

        if not is_valid(utility, weight, disponibility):
            capacity = int(input())
            break

        data.append({
            'id': index,
            'utility': utility,
            'weight': weight,
            'disponibility': disponibility,
            'ratio': utility / weight
        })

        index += 1

    return data, capacity

def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]['ratio']

    for j in range(low, high):
        if arr[j]['ratio'] > pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return (i + 1)


def quicksort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)

        quicksort(arr, low, pivot - 1)
        quicksort(arr, pivot + 1, high)

    return arr

def quicksort_simplified(arr):

    if len(arr) < 2:
        return arr

    pivot = arr[0]
    less = [i for i in arr[1:] if i['ratio'] <= pivot['ratio']]
    greater = [i for i in arr[1:] if i['ratio'] > pivot['ratio']]

    return quicksort(greater) + [pivot] + quicksort(less)


def get_best_items(data, capacity):
    items: list(tuple) = []

    for value in data:
        if (capacity - value['weight']) < 0:
            continue

        max_disponibility = value['disponibility']
        max_opportunity = capacity // value['weight']

        items.append((value['id'], min(max_opportunity, max_disponibility)))

        capacity -= min(max_opportunity, max_disponibility) * value['weight']

    return items
