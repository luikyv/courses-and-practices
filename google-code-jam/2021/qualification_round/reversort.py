import numpy as np

nb_examples = int(input())

for nb_case in range(nb_examples):
    nb_elements = int(input())
    elements = np.array(list(map(int, input().split())))
    
    cost = 0
    for i in range(len(elements) - 1):
        j = np.argmin(elements[i:]) + i

        sublist = elements[i:j+1]
        cost += len(sublist)
        elements = np.concatenate((elements[:i], sublist[::-1], elements[j+1:]))
    print(f"Case #{nb_case+1}: {cost}")