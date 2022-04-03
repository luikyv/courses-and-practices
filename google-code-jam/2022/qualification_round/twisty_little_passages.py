import random
import sys


def print_and_flush(str_):
    print(str_)
    sys.stdout.flush()


def estimate_paths(n_rooms, n_operations):
    rooms = random.sample(range(1, n_rooms + 1), n_rooms)
    _, n_total_paths = list(map(int, input().split(" ")))
    x = min(len(rooms), n_operations)
    # for i in range(x):
    # print_and_flush(f"T {rooms[i]}")
    print_and_flush(f"W")

    _, n_paths = list(map(int, input().split(" ")))
    n_total_paths += n_paths

    n_estimated_paths = int(n_rooms * (n_total_paths / (1 + 1)) / 2)
    print_and_flush(f"E {int(n_estimated_paths)}")

    # n_estimated_paths = int(n_rooms*(n_total_paths/(x+1))/2)
    # print_and_flush(f"E {int(n_estimated_paths)}")


n_examples = int(input())
for _ in range(n_examples):
    n_rooms, n_operations = list(map(int, input().split(" ")))
    estimate_paths(n_rooms, n_operations)
