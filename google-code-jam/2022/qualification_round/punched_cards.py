def print_punched_card(R, C):
    punched_card = list(R * f"{C*'+-'}+\n{C*'|.'}|\n" + f"{C*'+-'}+")
    (punched_card[0], punched_card[1], punched_card[2 * (C + 1)], punched_card[2 * (C + 1) + 1]) = ".", ".", ".", "."
    print("".join(punched_card))


n_examples = int(input())
for case_idx in range(1, n_examples + 1):
    R, C = list(map(int, input().split(" ")))
    print(f"Case #{case_idx}:")
    print_punched_card(R, C)
