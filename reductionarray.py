def goto(linenum):
    global line
    line = linenum

def mincostreduce(values):
    data = {}
    temp = []

    for val in values:
        print("In first one")
        for i in values[1:]:
            data.update({str(val) + str(i): val + i})

        minkey = min(data, key=data.get)

        results = [int(i) for i in list(str(minkey))]
        for k in results:
            values.remove(k)

    values.insert(0,data[minkey])
    temp.append(data[minkey])

    if len(values) != 1:
        total = sum(temp)
        mincostreduce(values)

    else:
        return 0

if __name__ == "__main__":
    values = [1, 2, 3]

    print(mincostreduce(values))
