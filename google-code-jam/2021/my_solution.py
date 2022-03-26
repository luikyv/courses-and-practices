import sys

import numpy as np


class Error(Exception):
    pass


def print_and_flush(str_):
    print(str_.replace(".0", ""))
    sys.stdout.flush()


def find_extreme(index_array):
    max_index, min_index = index_array[0], index_array[1]
    for i in range(2, len(index_array)):
        sub_index_array = np.array([max_index, min_index, index_array[i]])
        print_and_flush(" ".join(map(str, sub_index_array)))
        median_idx = int(input())
        if median_idx == -1:
            raise Error("Negative index")
        if len(sub_index_array[sub_index_array != median_idx]) != 2:
            raise Error(f"What??????????????????????/ {median_idx} {sub_index_array}")

        max_index, min_index = sub_index_array[sub_index_array != median_idx]

    return min_index


def compare_indexes(a, b, extreme):
    if a == extreme:
        return True
    if b == extreme:
        return False
    print_and_flush(" ".join(map(str, [a, b, extreme])))
    median_idx = int(input())
    if median_idx == -1:
        raise Error("Negative index")
    return a == median_idx


def merge_sort(index_array, compare_func, extreme):
    if len(index_array) in [0, 1]:
        return index_array

    idx = int(len(index_array) / 2)
    first_half = merge_sort(index_array[idx:], compare_func, extreme)
    second_half = merge_sort(index_array[:idx], compare_func, extreme)

    sorted_index_array = np.array([])
    while True:
        if len(first_half) == 0:
            sorted_index_array = np.concatenate([sorted_index_array, second_half])
            break
        if len(second_half) == 0:
            sorted_index_array = np.concatenate([sorted_index_array, first_half])
            break
        if compare_func(first_half[0], second_half[0], extreme):
            sorted_index_array = np.concatenate([sorted_index_array, [first_half[0]]])
            first_half = np.delete(first_half, 0)
        else:
            sorted_index_array = np.concatenate([sorted_index_array, [second_half[0]]])
            second_half = np.delete(second_half, 0)
    return sorted_index_array


n_test_cases, n_elements, n_total_questions = list(map(int, input().split(" ")))
for _ in range(n_test_cases):

    index_array = np.array(list(range(n_elements))) + 1
    extreme = find_extreme(index_array)

    sorted_index_array = merge_sort(index_array, compare_indexes, extreme)
    print_and_flush(" ".join(map(str, sorted_index_array)))
    if int(input()) != 1:
        raise Error("It didn't work")
