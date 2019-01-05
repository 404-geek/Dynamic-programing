import math

inp = int(input())
position = 0


def floor_log(num, base):
    if num < 0:
        raise ValueError("Non-negative number only.")

    if num == 0:
        return 0

    return base ** int(math.log(num, base))


def killer(a):
    if a == 1:
        return 1
    else:
        temp = floor_log(a, 2)
        return 2 * (a - temp) + 1


print(killer(inp))
