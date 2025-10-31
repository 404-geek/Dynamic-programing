def employeeFreeTime(schedule):

    schedule = [item for x in schedule for item in x]
    schedule.sort(key = lambda x: x[0])

    res = []

    merged_end = schedule[0][1]

    for j in range(1, len(schedule)):

        start, end = schedule[j]

        if start > merged_end:
            res.append([merged_end, start])
        else:
            merged_end = max(merged_end, end)

    return res

if __name__ == '__main__':
    print(employeeFreeTime(schedule= [[[1,3]], [[5,6]], [[2,8]], [[9,10]]]))