arr = []


def maximum(num, swapval, maxi):
    global h
    global arr

    if (swapval == 0):
        h = ''.join(str(e) for e in arr + num)
        print(h)
        return 0

    a = num.index(maxi)

    if num.index(maxi) <= swapval:
        num.remove(maxi)
        arr.append(maxi)
        maximum(num, swapval - a, max(num))


st = input()

num = list(map(int, st.split(" ")[0]))
swapval = int(st.split(" ")[1])
maxi = max(num)

maximum(num, swapval, maxi)
