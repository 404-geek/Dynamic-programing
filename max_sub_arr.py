def maximumSubarraySum(nums, k: int) -> int:
    seen = set()
    window_sum = 0
    max_sum = 0
    i = 0

    for j in range(len(nums)):
        # remove duplicates by shrinking left
        while nums[j] in seen:
            seen.remove(nums[i])
            window_sum -= nums[i]
            i += 1

        # add nums[j]
        seen.add(nums[j])
        window_sum += nums[j]

        # if window has size k
        if j - i + 1 == k:
            max_sum = max(max_sum, window_sum)
            # shrnk for next window
            seen.remove(nums[i])
            window_sum -= nums[i]
            i += 1

    return max_sum

print(maximumSubarraySum([1,5,4,2,9,9,9], 3))