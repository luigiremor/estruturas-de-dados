
from desafios.mochila.problema_da_mochila import get_data, get_best_items, quicksort

def main():
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

    data, capacity = get_data()
    data = quicksort(data)
    items = get_best_items(data, capacity)


    for item in items:
        print(item[0], item[1])

if __name__ == "__main__":
    main()