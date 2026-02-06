def insertion_sort(arr):
    """
    Insertion Sort Algorithm

    Description:
    Insertion Sort builds the final sorted list one element at a time.
    It takes each element and inserts it into its correct position
    among the already sorted elements on the left side of the list.

    Time Complexity:
    - Worst case: O(n^2) when the list is sorted in reverse order.
    - Average case: O(n^2).
    - Best case: O(n) when the list is already sorted or nearly sorted.

    Space Complexity:
    - O(n) due to copying the input list to avoid modifying the original one.
    """
    
    arr = arr.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr
