list = ["civic", "level", "kayak", "madam", "tacocat", "racecar", "student", "rotor", "problem", "brick"]
for c in range(len(list)):
    word = list[c]
    wlen = len(word) - 1
    print(word[0], word[wlen])
for d in range(len(list)):
    word = list[d]
    wlen = len(word) - 2
    print(word[1], word[wlen])
