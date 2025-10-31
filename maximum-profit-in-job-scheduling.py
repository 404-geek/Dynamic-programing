from bisect import bisect_left


def jobScheduling(startTime, endTime, profit):
    jobs = sorted(zip(startTime, endTime, profit))
    n = len(jobs)
    dp = [0] * (n + 1)

    for i in range(n - 1, -1, -1):
        _, end, prof = jobs[i]
        next_job = bisect_left(jobs, end, lo=i + 1, key=lambda x: x[0])
        dp[i] = max(dp[i + 1], prof + dp[next_job])

    return dp[0]

jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70])