
def insertIntervals(intervals, newInterval):

    in_start = newInterval[0]
    in_end = newInterval[1]
    n = len(intervals)

    res = []
    i = 0

    while i < n and intervals[i][1] < in_start:
        res.append(intervals[i])
        i+=1

    while i < n and intervals[i][0] <= in_end:
        in_start = min(in_start, intervals[i][0])
        in_end = max(in_end, intervals[i][1])

        i+=1

    res.append([in_start, in_end])

    for j in range(i, n):
        res.append(intervals[j])

    return res


print(insertIntervals([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8] ))