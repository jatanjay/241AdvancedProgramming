"""
file : quicksort.py
File contains function partion for quick sort algorithm that will be used in main file.
"""


def partition(arr, start_index, end_index):
    midpoint = start_index + (end_index - start_index) // 2
    pivot = arr[midpoint].title
    low = start_index
    high = end_index

    done = False
    while not done:
        while arr[low].title < pivot:
            low += 1

        while pivot < arr[high].title:
            high -= 1

        if low >= high:
            done = True

        else:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1

    return high


def quickS(array, start_index, end_index):
    """
    :param array:
    :type array:
    :param start_index:
    :type start_index:
    :param end_index:
    :type end_index:
    :return:
    :rtype:
    """
    partition(array, start_index, end_index)

    if end_index <= start_index:
        return

    high = partition(array, start_index, end_index)
    quickS(array, start_index, high)
    quickS(array, high + 1, end_index)
