def removeDuplicates(nums) -> int:
    i = 0
    j = i + 1
    cnt = 0

    while j < len(nums):

        if nums[i] < nums[j]:
            cnt += 1
            nums[cnt] = nums[j]
            i = cnt

        j += 1

    print(nums)
    return cnt


print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))