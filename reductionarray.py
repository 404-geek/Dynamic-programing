def mincostreduce(values,j):

    data = {}
    temp = []

    for val in values:
        for i in values[1:]:
            data.update({str(val) + str(i): val + i})

        minkey = min(data, key=data.get)

        results = [int(i) for i in list(str(minkey))]

        for k in results:
            print(results)
            values.remove(k)
            
    print(results)
    values.insert(0,data[minkey])

    j= data[minkey]+j

    print(j)

    if len(values) != 1:
        mincostreduce(values,j)


if __name__ == "__main__":
    values = [1, 2, 3, 4]

    print(mincostreduce(values,0))
