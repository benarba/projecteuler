units = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
tens = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]
thousand = 8
teens = {
    10: 3,
    11: 6,
    12: 6,
    13: 8,
    14: 8,
    15: 7,
    16: 7,
    17: 9,
    18: 8,
    19: 8,
}


def get_tens(i):
    i = i % 100
    if i in teens:
        return teens[i]
    return tens[int(i / 10)] + units[i % 10]


sum = 0
for i in range(1, 1000):
    count = 0
    h = int(i / 100)
    t = i % 100

    if h > 0:
        number_of_hundreds = units[h]
        count += number_of_hundreds
        count += 7
    if h > 0 and i % 100 != 0:
        count += 3
    count += get_tens(t)
    sum += count

sum += 11

print(sum)
