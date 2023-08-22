import unittest
from .problema_da_mochila import quicksort, get_best_items


class TestProblemaDaMochila(unittest.TestCase):

    def test_quicksort(self):
        data = [
            {'id': 0, 'utility': 18, 'weight': 5, 'disponibility': 1, 'ratio': 3.6},
            {'id': 1, 'utility': 12, 'weight': 4, 'disponibility': 2, 'ratio': 3},
            {'id': 2, 'utility': 15, 'weight': 5, 'disponibility': 3, 'ratio': 3},
            {'id': 3, 'utility': 10, 'weight': 2, 'disponibility': 2, 'ratio': 5},
            {'id': 4, 'utility': 15, 'weight': 6, 'disponibility': 5, 'ratio': 2.5},
            {'id': 5, 'utility': 4, 'weight': 2, 'disponibility': 5, 'ratio': 2}
        ]

        sorted_data = quicksort(arr=data, low=0, high=len(data) - 1)
        self.assertEqual(sorted_data, [
            {'id': 3, 'utility': 10, 'weight': 2, 'disponibility': 2, 'ratio': 5},
            {'id': 0, 'utility': 18, 'weight': 5, 'disponibility': 1, 'ratio': 3.6},
            {'id': 1, 'utility': 12, 'weight': 4, 'disponibility': 2, 'ratio': 3},
            {'id': 2, 'utility': 15, 'weight': 5, 'disponibility': 3, 'ratio': 3},
            {'id': 4, 'utility': 15, 'weight': 6, 'disponibility': 5, 'ratio': 2.5},
            {'id': 5, 'utility': 4, 'weight': 2, 'disponibility': 5, 'ratio': 2}
        ])

    def test_get_best_items(self):
        data = [
            {'id': 3, 'utility': 10, 'weight': 2, 'disponibility': 2, 'ratio': 5},
            {'id': 0, 'utility': 18, 'weight': 5, 'disponibility': 1, 'ratio': 3.6},
            {'id': 1, 'utility': 12, 'weight': 4, 'disponibility': 2, 'ratio': 3},
            {'id': 2, 'utility': 15, 'weight': 5, 'disponibility': 3, 'ratio': 3},
            {'id': 4, 'utility': 15, 'weight': 6, 'disponibility': 5, 'ratio': 2.5},
            {'id': 5, 'utility': 4, 'weight': 2, 'disponibility': 5, 'ratio': 2}
        ]

        capacity = 20
        items = get_best_items(data, capacity)
        self.assertEqual(items, [
            (3, 2),
            (0, 1),
            (1, 2),
            (5, 1)
        ])
