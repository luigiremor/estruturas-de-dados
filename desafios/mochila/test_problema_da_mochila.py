import unittest
from .problema_da_mochila import quicksort, get_best_items, quicksort_simplified

class TestProblemaDaMochila(unittest.TestCase):

    def setUp(self):
        self.data = [
            {'id': 0, 'utility': 18, 'weight': 5, 'disponibility': 1, 'ratio': 3.6},
            {'id': 1, 'utility': 12, 'weight': 4, 'disponibility': 2, 'ratio': 3},
            {'id': 2, 'utility': 15, 'weight': 5, 'disponibility': 3, 'ratio': 3},
            {'id': 3, 'utility': 10, 'weight': 2, 'disponibility': 2, 'ratio': 5},
            {'id': 4, 'utility': 15, 'weight': 6, 'disponibility': 5, 'ratio': 2.5},
            {'id': 5, 'utility': 4, 'weight': 2, 'disponibility': 5, 'ratio': 2}
        ]

        self.capacity = 20

        self.sorted_data = [
            {'id': 3, 'utility': 10, 'weight': 2, 'disponibility': 2, 'ratio': 5},
            {'id': 0, 'utility': 18, 'weight': 5, 'disponibility': 1, 'ratio': 3.6},
            {'id': 1, 'utility': 12, 'weight': 4, 'disponibility': 2, 'ratio': 3},
            {'id': 2, 'utility': 15, 'weight': 5, 'disponibility': 3, 'ratio': 3},
            {'id': 4, 'utility': 15, 'weight': 6, 'disponibility': 5, 'ratio': 2.5},
            {'id': 5, 'utility': 4, 'weight': 2, 'disponibility': 5, 'ratio': 2}
        ]

        """
         5 1 5
        10 1 5
        20 2 2
        30 3 3
        40 4 2
        50 5 2
        -1 -1 -1
        20
        """

        self.data2 = [
            {'id': 0, 'utility': 5, 'weight': 1, 'disponibility': 5, 'ratio': 5},
            {'id': 1, 'utility': 10, 'weight': 1, 'disponibility': 5, 'ratio': 10},
            {'id': 2, 'utility': 20, 'weight': 2, 'disponibility': 2, 'ratio': 10},
            {'id': 3, 'utility': 30, 'weight': 3, 'disponibility': 3, 'ratio': 10},
            {'id': 4, 'utility': 40, 'weight': 4, 'disponibility': 2, 'ratio': 10},
            {'id': 5, 'utility': 50, 'weight': 5, 'disponibility': 2, 'ratio': 10}
        ]

        self.sorted_data2 = [
            {'id': 5, 'utility': 50, 'weight': 5, 'disponibility': 2, 'ratio': 10},
            {'id': 4, 'utility': 40, 'weight': 4, 'disponibility': 2, 'ratio': 10},
            {'id': 3, 'utility': 30, 'weight': 3, 'disponibility': 3, 'ratio': 10},
            {'id': 2, 'utility': 20, 'weight': 2, 'disponibility': 2, 'ratio': 10},
            {'id': 1, 'utility': 10, 'weight': 1, 'disponibility': 5, 'ratio': 10},
            {'id': 0, 'utility': 5, 'weight': 1, 'disponibility': 5, 'ratio': 5}
        ]

        self.capacity2 = 20

        self.result2 = [
            (5, 2),
            (4, 2),
            (1, 2),
        ]
        
    def test_quicksort(self):
        data = quicksort(arr=self.data, low=0, high=len(self.data) - 1)
        self.assertEqual(data, self.sorted_data)

        # data2 = quicksort(arr=self.data2, low=0, high=len(self.data2) - 1)
        # self.assertEqual(data2, self.sorted_data2)

    def test_quicksort_simplified(self):
        sorted_data = quicksort_simplified(arr=self.data)
        self.assertEqual(sorted_data, self.sorted_data)

        sorted_data2 = quicksort_simplified(arr=self.data2)
        self.assertEqual(sorted_data2, self.sorted_data2)

    # def test_all_quicksorts(self):
    #     sorted_data = quicksort(arr=self.data2, low=0, high=len(self.data2) - 1)
    #     sorted_data2 = quicksort_simplified(arr=self.data2)

    #     # self.assertEqual(sorted_data, sorted_data2)
    #     # self.assertEqual(sorted_data, self.sorted_data2)
    #     self.assertEqual(sorted_data2, self.sorted_data2)


    # def test_get_best_items_with_both_quicksorts(self):
    #     sorted_data = quicksort(arr=self.data2, low=0, high=len(self.data2) - 1)
    #     sorted_data2 = quicksort_simplified(arr=self.data2)

    #     items = get_best_items(sorted_data, self.capacity2)
    #     items2 = get_best_items(sorted_data2, self.capacity2)

    #     # self.assertEqual(items, items2)

    #     self.assertEqual(items2, self.result2)

    # def test_get_best_items(self):
    #     items = get_best_items(self.sorted_data, self.capacity)
    #     self.assertEqual(items, [
    #         (3, 2),
    #         (0, 1),
    #         (1, 2),
    #         (5, 1)
    #     ])

    #     items2 = get_best_items(self.sorted_data2, self.capacity2)
    #     self.assertEqual(items2, [
    #         (5, 2),
    #         (4, 2),
    #         (1, 2),
    #     ])
