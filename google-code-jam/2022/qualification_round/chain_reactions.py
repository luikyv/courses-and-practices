import numpy as np


def calculate_fun(
    fun_factors,
    pointers,
    target=0,
):
    if target not in pointers:
        return fun_factors[target - 1], fun_factors[target - 1]
    current_min_max = np.inf
    fun_factor_sum = 0
    for i in range(1, len(pointers) + 1):
        if pointers[i - 1] == target:
            current_max_, fun_factor = calculate_fun(fun_factors, pointers, i)
            fun_factor_sum += fun_factor
            if current_max_ < current_min_max:
                current_min_max = current_max_
    if target == 0:
        result = -1, fun_factor_sum
    else:
        result = (
            (fun_factors[target - 1], fun_factors[target - 1] + fun_factor_sum - current_min_max)
            if fun_factors[target - 1] > current_min_max
            else (current_min_max, fun_factor_sum)
        )

    return result


n_examples = int(input())
for case_idx in range(1, n_examples + 1):
    n_modules = int(input())
    fun_factors = np.array(list(map(int, input().split())))
    pointers = np.array(list(map(int, input().split())))

    print(f"Case #{case_idx}: {calculate_fun(fun_factors, pointers)[1]}")
