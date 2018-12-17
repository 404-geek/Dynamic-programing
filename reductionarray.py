reduce=0
def mincostreduce(values, j):
    global reduce

    rem = min(values[1:])
    tem = values[0] + rem

    values.remove(values[0])
    values.remove(rem)

    values.insert(0,tem)
    result = j+tem

    reduce = result

    if len(values) != 1:
        mincostreduce(1*values,result)

    return reduce




if __name__ == "__main__":
    values = []

    print(mincostreduce(values, 0))
