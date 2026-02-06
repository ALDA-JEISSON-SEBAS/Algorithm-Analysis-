def merge_sort(array):
    """
    Merge Sort Algorithm

    Description:
    This algorithm follows the divide-and-conquer paradigm.
    It recursively splits the array into two halves, sorts each half,
    and then merges the sorted halves into a single sorted array.

    Time Complexity:
        Best Case: O(n log n)
        Average Case: O(n log n)
        Worst Case: O(n log n)

    Space Complexity:
        O(n) due to the use of auxiliary arrays during the merge step.
    """

    # Base case: an array with 0 or 1 element is already sorted
    if len(array) <= 1:
        return array

    # Split the array into two halves
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    # Merge the two sorted halves
    return merge(left, right)


def merge(left, right):
    """
    Merges two sorted arrays into one sorted array.
    """

    result = []
    i = j = 0

    # Compare elements from both arrays and append the smallest one
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result
