def preprocess(word):
    letters = []
    for c in word:
        if letters and letters[-1][0] == c:
            letters[-1][1] += 1
        else:
            letters.append([c, 1])
    return letters


def solve(word):
    letters = preprocess(word)
    for i in range(len(letters) - 1):
        if letters[i][0] < letters[i + 1][0]:
            letters[i][1] *= 2
    return "".join([letter[0] * letter[1] for letter in letters])


nb_examples = int(input())

for case_idx in range(nb_examples):
    word = input()
    print(f"Case #{case_idx+1}: {solve(word)}")
