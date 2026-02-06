import unittest
from algorithms.insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(insertion_sort([]), [])

    def test_single_element(self):
        self.assertEqual(insertion_sort([1]), [1])

    def test_unsorted_list(self):
        data = [5, 3, 1, 4, 2]
        self.assertEqual(insertion_sort(data), [1, 2, 3, 4, 5])

    def test_duplicates(self):
        data = [3, 1, 2, 3, 1]
        self.assertEqual(insertion_sort(data), [1, 1, 2, 3, 3])


if __name__ == "__main__":
    unittest.main()
