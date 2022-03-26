import sys
import math
import numpy as np
import logging
class Error(Exception):
    pass

def print_and_flush(str_):
    print(str_)
    sys.stdout.flush()

def find_median(a, b, c):
    print_and_flush(
        " ".join(map(str, [a, b, c]))
    )
    median = int(input())
    if median == -1: raise Error(f"Negative index. Arguments: {' '.join(map(str, [a, b, c]))}")
    return median

def binary_insert(sorted_array, element, reference):

    left_idx = 0
    right_idx = len(sorted_array) - 1
    middle_idx = math.floor((left_idx+right_idx)/2)
    while True:
        if middle_idx == 0:
            median_element = (
                find_median(reference, sorted_array[1], element)
            )
            return (
                np.concatenate([[element], sorted_array])
                if median_element == reference
                else (
                    np.concatenate([sorted_array[:2], [element], sorted_array[2:]])
                    if sorted_array[1] == median_element
                    else np.concatenate([sorted_array[:1], [element], sorted_array[1:]])
                )
            )
        else:
            median_element = (
                find_median(reference, sorted_array[middle_idx], element)
            )
            if median_element == reference:
                return np.concatenate([[element], sorted_array])

        if median_element == element:
            right_idx = middle_idx - 1
        else:
            left_idx = middle_idx + 1

        if right_idx < left_idx: break
        middle_idx = math.floor((left_idx+right_idx)/2)
    return (
        np.concatenate([sorted_array[:left_idx], np.array([element]), sorted_array[left_idx:]])
    )

def binary_sort(input_array):
    median_idx = find_median(*input_array[:3])
    reference, max_idx = input_array[:3][ input_array[:3] != median_idx ]
    sorted_array = np.array([reference, median_idx, max_idx])
    for i in range(3, len(input_array)):
        sorted_array = binary_insert(sorted_array, input_array[i], sorted_array[0])
    return sorted_array

n_test_cases, n_elements, n_total_questions = list(map(int, input().split(" ")))
for i in range(n_test_cases):
    index_array = np.array(list(range(n_elements))) + 1
    sorted_array = binary_sort(index_array)

    print_and_flush(
        " ".join(map(str, sorted_array))
    )
    if int(input()) != 1: raise Error("It didn't work")
