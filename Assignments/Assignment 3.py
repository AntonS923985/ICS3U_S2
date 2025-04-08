list = ["civic", "level", "kayak", "madam", "tacocat", "racecar", "student", "rotor", "problem", "brick"]
for c in range(len(list)):
    word = list[c]
    wlen = len(word) - 1
    for d in range(len(word)):
      print(word[d], word[wlen-d])
