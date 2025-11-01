def intervalIntersection(firstList, secondList):

    i, j = 0, 0
    res = []

    while i < len(firstList) and j < len(secondList):

        a = max(firstList[i][0], secondList[j][0])
        b = min(firstList[i][1], secondList[j][1])

        if a <= b:
            res.append([a, b])

        if firstList[i][1] < secondList[j][1]:
            i+=1
        else:
            j+=1

    return res

print(intervalIntersection(firstList=[[0,2],[5,10],[13,23],[24,25]],
                     secondList=[[1,5],[8,12],[15,24],[25,26]]))


