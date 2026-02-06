import unittest
from algorithms.bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(bubble_sort([]), [])

    def test_single_element(self):
        self.assertEqual(bubble_sort([1]), [1])

    def test_unsorted_list(self):
        data = [5, 3, 1, 4, 2]
        self.assertEqual(bubble_sort(data), [1, 2, 3, 4, 5])

    def test_duplicates(self):
        data = [3, 1, 2, 3, 1]
        self.assertEqual(bubble_sort(data), [1, 1, 2, 3, 3])


if __name__ == "__main__":
    unittest.main()
