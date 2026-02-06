def selection_sort(array):
    """
    Selection Sort Algorithm

    Description:
    This algorithm repeatedly selects the smallest element from
    the unsorted portion of the array and swaps it with the first
    unsorted position.

    Time Complexity:
        Best Case: O(n^2)
        Average Case: O(n^2)
        Worst Case: O(n^2)

    Space Complexity:
        O(1) since the algorithm sorts the array in place.
    """

    n = len(array)

    # Traverse through all elements of the array
    for i in range(n):

        # Assume the current index holds the minimum element
        min_idx = i

        # Find the minimum element in the remaining unsorted array
        for j in range(i + 1, n):
            if array[j] < array[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first unsorted element
        array[i], array[min_idx] = array[min_idx], array[i]

    return array
