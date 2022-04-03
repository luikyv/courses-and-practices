import random
import sys


def print_and_flush(str_):
    print(str_)
    sys.stdout.flush()


def estimate_paths(n_rooms, n_operations):

    unseen_node_indexes = set(random.sample(range(1, n_rooms + 1), n_rooms))
    current_node, degree = list(map(int, input().split(" ")))

    unseen_node_indexes -= set([current_node])
    degree_sum = degree
    lowly_connected_degree_sum = degree
    lowly_connected_degree_counter = 1

    for i in range(n_operations):
        if i % 2 == 0:
            print_and_flush("W")
            current_node, degree = list(map(int, input().split(" ")))
            if current_node in unseen_node_indexes:
                unseen_node_indexes -= set([current_node])
                degree_sum += degree
        else:
            print_and_flush(f"T {unseen_node_indexes.pop()}")
            _, degree = list(map(int, input().split(" ")))
            lowly_connected_degree_sum += degree
            lowly_connected_degree_counter += 1
            degree_sum += degree

    lowly_connected_degree_mean = lowly_connected_degree_sum / lowly_connected_degree_counter
    n_estimated_paths = (degree_sum + lowly_connected_degree_mean * len(unseen_node_indexes)) / 2
    print_and_flush(f"E {int(n_estimated_paths)}")


n_examples = int(input())
for _ in range(n_examples):
    n_rooms, n_operations = list(map(int, input().split(" ")))
    estimate_paths(n_rooms, n_operations)
