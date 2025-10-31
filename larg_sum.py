
def maxSubArray( nums) -> int:
    curr_sum = 0
    max_sum = nums[0]

    for i in nums:

        if curr_sum < 0:
            curr_sum = 0

        curr_sum += i

        max_sum = max(curr_sum, max_sum)

    return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
