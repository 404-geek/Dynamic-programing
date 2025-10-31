from collections import deque


def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    if len(nums) <= k:
        return [max(nums)]

    start = 0

    max_list = []

    dq = deque()

    for end in range(len(nums)):
        # Remove elements smaller than current from back
        while dq and nums[dq[-1]] < nums[end]:
            dq.pop()

        dq.append(end)

        # Remove front if it's out of window
        if dq[0] < start:
            dq.popleft()

        # Once we've reached window size k, record the current max
        if end - start + 1 == k:
            max_list.append(nums[dq[0]])
            start += 1  # slide window by one

    return max_list

print(maxSlidingWindow([1,3,1,2,0,5], 3))