from algorithms.quick_sort import quick_sort


def test_quick_sort_empty():
    assert quick_sort([]) == []


def test_quick_sort_single_element():
    assert quick_sort([5]) == [5]


def test_quick_sort_sorted():
    assert quick_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_quick_sort_reverse():
    assert quick_sort([4, 3, 2, 1]) == [1, 2, 3, 4]


def test_quick_sort_duplicates():
    assert quick_sort([3, 1, 2, 3, 1]) == [1, 1, 2, 3, 3]


def test_quick_sort_negative_numbers():
    assert quick_sort([0, -2, 5, -1]) == [-2, -1, 0, 5]
