def get_month_days(m, y):
    month_days = 0
    if m in {4, 6, 9, 11}:
        month_days = 30
    elif m == 2:
        if y % 400 == 0 or y % 4 != 0:
            month_days = 28
        else:
            month_days = 29
    else:
        month_days = 31
    return month_days


count = 0
month_start = 0
for y in range(1900, 2001):
    for m in range(1, 13):
        if y == 1900 and m == 1:
            continue
        month_days = get_month_days(m, y)
        month_start = (month_start + (month_days % 7)) % 7
        if y >= 1901 and month_start == 6:
            count += 1

print(count)
