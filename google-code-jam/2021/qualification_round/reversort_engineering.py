import numpy as np

def calculate_worst_cost(list_size):
    return sum(list(range(2, list_size+1)))

def calculate_best_cost(list_size):
    return list_size - 1

def increase_cost(sorted_np_array, cost_increase):

    if cost_increase == 0: return sorted_np_array
    array_length = len(sorted_np_array)
    increasable_cost = min(cost_increase, array_length - 1)
    return np.concatenate([
        increase_cost(sorted_np_array[1:increasable_cost+1], cost_increase-increasable_cost)[::-1],
        [sorted_np_array[0]],
        sorted_np_array[increasable_cost + 1:],
    ])

nb_examples = int(input())
for i in range(nb_examples):
    list_size, goal_cost = list(map(int, input().split(" ")))
    best_cost = calculate_best_cost(list_size)
    worst_cost = calculate_worst_cost(list_size)

    if goal_cost < best_cost or goal_cost > worst_cost:
        print(f"Case #{i+1}: IMPOSSIBLE")
        continue

    sorted_np_array = np.array(list(range(list_size))) + 1
    matching_goal_np_array = increase_cost(sorted_np_array, goal_cost - best_cost)
    print(f"Case #{i+1}: {' '.join(map(str, matching_goal_np_array))}")
