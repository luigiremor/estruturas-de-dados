"""
 18 5 1
12 4 2
15 5 3
10 2 2
15 6 5
4 2 5
-1 -1 -1
20


3 2
0 1
1 2
5 1
"""


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


def quicksort(arr):

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


data, capacity = get_data()
data = quicksort(data)
items = get_best_items(data, capacity)


for item in items:
    print(item[0], item[1])
