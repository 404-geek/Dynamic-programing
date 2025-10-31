def eraseOverlapIntervals(intervals) -> int:
    intervals.sort(key=lambda x: x[1])
    end = intervals[0][1]
    cnt = 1

    print(intervals)

    for i in range(1, len(intervals)):

        if intervals[i][0] >= end:
            end = intervals[i][1]
            cnt += 1

    print(cnt)

    return len(intervals) - cnt

eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]])