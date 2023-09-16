import unittest

from desafios.caixeiro_viajante.caixeiro_viajante import main


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.input_data = [
            "0 0",
            "10 10",
            "0 20",
            "20 20",
            "0 10",
            "10 0",
            "-1 -1"
        ]

        self.input_data2 = [
            "88 36",
            "62 23",
            "61 55",
            "96 55",
            "64 26",
            "31 90",
            "7 93",
            "59 85",
            "41 67",
            "36 28",
            "13 2",
            "93 25",
            "25 86",
            "12 9",
            "16 86",
            "23 88",
            "8 69",
            "13 4",
            "56 48",
            "35 25",
            "87 14",
            "3 66",
            "94 59",
            "16 42",
            "57 43",
            "20 88",
            "84 42",
            "38 14",
            "40 11",
            "28 43",
            "-1 -1"
        ]

    def test_improve(self):
        original_cost, improved_cost = main(self.input_data)
        self.assertEqual(original_cost, "94.79")
        self.assertEqual(improved_cost, "74.14")

    def test_improve2(self):
        original_cost, improved_cost = main(self.input_data2)
        self.assertEqual(original_cost, "1559.87")
        self.assertEqual(improved_cost, "1134.83")
