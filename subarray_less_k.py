def numSubarrayProductLessThanK(nums, k: int) -> int:
    start = 0

    run_prod = 1

    cnt = 0

    for end in range(len(nums)):

        run_prod *= nums[end]

        while start < end and run_prod >= k:
            run_prod //= nums[start]
            start += 1

        cnt += end - start + 1

    return cnt

print(numSubarrayProductLessThanK(nums = [10,5,2,6], k = 100))