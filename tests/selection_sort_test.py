from algorithms.selection_sort import selection_sort


def test_selection_sort_empty():
    assert selection_sort([]) == []


def test_selection_sort_single_element():
    assert selection_sort([10]) == [10]


def test_selection_sort_sorted():
    assert selection_sort([1, 2, 3]) == [1, 2, 3]


def test_selection_sort_reverse():
    assert selection_sort([3, 2, 1]) == [1, 2, 3]


def test_selection_sort_duplicates():
    assert selection_sort([4, 1, 4, 2]) == [1, 2, 4, 4]


def test_selection_sort_negative_numbers():
    assert selection_sort([-5, 3, 0]) == [-5, 0, 3]
