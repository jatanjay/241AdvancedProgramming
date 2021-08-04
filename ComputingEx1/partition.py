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
