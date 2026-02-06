def quick_sort(arr):
    """
    Quick Sort Algorithm

    Description:
    This algorithm selects a pivot element and partitions the array
    into two sub-arrays: elements less than or equal to the pivot
    and elements greater than the pivot. Each sub-array is then
    sorted recursively.

    Time Complexity:
        Best Case: O(n log n)
        Average Case: O(n log n)
        Worst Case: O(n^2), occurs when the pivot produces highly unbalanced partitions.

    Space Complexity:
        O(n) due to recursion and creation of new sub-arrays.
    """

    # Base case: arrays of size 0 or 1 are already sorted
    if len(arr) <= 1:
        return arr

    # Choose the pivot (last element)
    pivot = arr[-1]

    # Partition the array based on the pivot
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    # Recursively sort partitions and combine results
    return quick_sort(left) + [pivot] + quick_sort(right)
