import numpy as np

def compute_cost(input_array, cost_cj, cost_jc):
    input_str = "".join(input_array).replace("?", "")
    return input_str.count("CJ") * cost_cj + input_str.count("JC") * cost_jc 

def find_next_letter_idx(input_array):
    symbol_locations = np.where(input_array=="C" or input_array=="J")
    if symbol_locations[0].size == 0: return None
    return symbol_locations[0][0]

def replace_quotes(input_array):
    idx_start = 0
    idx_end = 0
    while idx_end < input_array.size:

        break_flag = False
        for i in range(idx_start, input_array.size):
            if input_array[i] == "?":
                idx_start = i
                break_flag = True
                break
        if not break_flag: return
        
        idx_end = idx_start
        for j in range(idx_start+1, input_array.size):
            if input_array[j] in ["C", "J"]:
                break
            idx_end = j
        
        left_side = input_array[idx_start-1] if idx_start > 0 else None
        right_side = input_array[idx_end+1] if idx_end < input_array.size - 1 else None

        if left_side:
            input_array[idx_start:idx_end+1] = np.array([left_side]*(idx_end+1-idx_start))
        elif right_side:
            input_array[idx_start:idx_end+1] = np.array([right_side]*(idx_end+1-idx_start))
        else:
            input_array[idx_start:idx_end+1] = np.array(["C"]*(idx_end+1-idx_start))

        idx_start = idx_end + 1


nb_examples = int(input())
for i in range(nb_examples):
    input_array = input().split()
    cost_cj, input_array = int(input_array[0]), input_array[1:]
    cost_jc, input_array = int(input_array[0]), input_array[1:]

    input_array = np.array(list(input_array[0]))
    replace_quotes(input_array)
    print(f"Case #{i+1}: {compute_cost(input_array, cost_cj, cost_jc)}")