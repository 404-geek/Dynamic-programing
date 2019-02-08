def solver(arr,val):
    res = []
    maxi = max(arr)
    arr.remove(maxi)
    res.append(maxi)
    for i in arr:
        if maxi+i <= val:
            res = list(filter(lambda a: a > i, res))
            if (sum(res) <= val):
                res.append(i)

    return res


if __name__ == '__main__':
    arr = [1,2,3,2,3,4,1,2,3]
    val = 6
    print(solver(arr,val))