from dataclasses import dataclass

import numpy as np


@dataclass
class Printer:
    ciano: int
    magenta: int
    yellow: int
    black: int


def balance_color(printer_1, printer_2, printer_3):
    max_ciano = min([printer_1.ciano, printer_2.ciano, printer_3.ciano])
    max_magenta = min([printer_1.magenta, printer_2.magenta, printer_3.magenta])
    max_yellow = min([printer_1.yellow, printer_2.yellow, printer_3.yellow])
    max_black = min([printer_1.black, printer_2.black, printer_3.black])

    color_amount = 0
    max_colors = [max_ciano, max_magenta, max_yellow, max_black]
    for i in range(len(max_colors)):
        if color_amount + max_colors[i] >= 10**6:
            max_colors[i] = 10**6 - color_amount
            return " ".join(
                map(
                    str,
                    np.concatenate([np.array(max_colors[: i + 1]), np.zeros(len(max_colors) - i - 1)]).astype("int64"),
                ),
            )
        else:
            color_amount += max_colors[i]
    return "IMPOSSIBLE"


n_examples = int(input())
for case_idx in range(1, n_examples + 1):
    printer_1 = Printer(*list(map(int, input().split(" "))))
    printer_2 = Printer(*list(map(int, input().split(" "))))
    printer_3 = Printer(*list(map(int, input().split(" "))))
    result = balance_color(
        printer_1,
        printer_2,
        printer_3,
    )
    print(f"Case #{case_idx}: {result}")
