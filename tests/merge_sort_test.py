from algorithms.merge_sort import merge_sort


def test_merge_sort_empty():
    assert merge_sort([]) == []


def test_merge_sort_single_element():
    assert merge_sort([7]) == [7]


def test_merge_sort_sorted():
    assert merge_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_merge_sort_reverse():
    assert merge_sort([4, 3, 2, 1]) == [1, 2, 3, 4]


def test_merge_sort_duplicates():
    assert merge_sort([5, 2, 5, 1]) == [1, 2, 5, 5]


def test_merge_sort_negative_numbers():
    assert merge_sort([-3, 0, -1, 2]) == [-3, -1, 0, 2]
