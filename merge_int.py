def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    res = [intervals[0]]

    for i in range(1, len(intervals)):

        if res[-1][1] >= intervals[i][0]:
            res[-1][0] = min(res[-1][0], intervals[i][0])
            res[-1][1] = max(res[-1][1], intervals[i][1])

        else:
            res.append(intervals[i])

    return res

merge([[1,3],[2,6],[8,10],[15,18]])

