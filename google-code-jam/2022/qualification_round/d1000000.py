import numpy as np


def find_straight(dice_list):
    dice_list = np.sort(dice_list)
    if dice_list[0] >= len(dice_list):
        return len(dice_list)
    straight_counter = 0
    for min_dice in dice_list:
        if min_dice > straight_counter:
            straight_counter += 1

    return straight_counter


n_examples = int(input())
for case_idx in range(1, n_examples + 1):

    _ = int(input())
    dice_list = np.array(list(map(int, input().split())))
    result = find_straight(dice_list)
    print(f"Case #{case_idx}: {result}")
