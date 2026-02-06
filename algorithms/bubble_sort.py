def bubble_sort(arr):
    """
    Bubble Sort Algorithm

    Description:
    Bubble Sort repeatedly steps through the list, compares adjacent elements,
    and swaps them if they are in the wrong order. This process is repeated
    until the list is sorted. Larger elements "bubble up" to the end of the list.

    Time Complexity:
    - Worst case: O(n^2) when the list is in reverse order.
    - Average case: O(n^2).
    - Best case: O(n^2) in this implementation (no early stopping optimization).

    Space Complexity:
    - O(n) due to copying the input list to avoid modifying the original one.
    """
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
