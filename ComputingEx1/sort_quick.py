"""
file : quicksort.py
Author : Jatan Pandya
File contains function partition for quick sort algorithm that will be used in main file.
reference : ZYBooks / chapter
"""


def partition(arr, start_index, end_index):
    """
    :param arr: input array
    :type arr: list
    :param start_index: starting index, usually list[0]
    :type start_index: int
    :param end_index: end index
    :type end_index: int
    :return: high index. The last index in the left segment.
    :rtype: int
    """
    midpoint = start_index + (end_index - start_index) // 2
    pivot = arr[midpoint].title  # since sorting by song title
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
    :param array: input array
    :type array: list
    :param start_index: starting index
    :type start_index: int
    :param end_index: ending index
    :type end_index: int
    :return: nil
    :rtype: nil
    """
    partition(array, start_index, end_index)  # call partition() on arr

    if start_index >= end_index:
        return

    high = partition(array, start_index, end_index)
    quickS(array, start_index, high - 1)
    quickS(array, high + 1, end_index)
