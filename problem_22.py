with open("0022_names.txt") as f:
    names = [name.strip('"').lower() for name in f.readline().split(",")]

names = sorted(names)

sum = 0
for i in range(len(names)):
    name = names[i]
    letter_sum = 0
    for j in range(len(name)):
        letter_sum += ord(name[j]) - ord("a") + 1
    sum += letter_sum * (i + 1)


print(sum)
