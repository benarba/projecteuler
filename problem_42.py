def word_value(word):
    chars = list(word)
    value = 0
    for c in chars:
        value += ord(c) - ord("A") + 1
    return value


with open("0042_words.txt", "r") as f:
    lines = f.readline()

words = [word.strip('"') for word in lines.split(",")]


max_tri = 1
max_diff = 1
set_tri = {1}

count = 0
for word in words:
    value = word_value(word)
    while value > max_tri:
        max_diff += 1
        max_tri += max_diff
        set_tri.add(max_tri)

    if value in set_tri:
        count += 1

print(f"count: {count}")
