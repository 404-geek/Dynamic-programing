def maxSubsetSum(arr):
    incl = 0
    excl = 0

    for i in arr:

        temp = incl

        incl = max(incl,excl+i)

        excl = temp

    return incl

nums = [2, 1, 5, 8, 4]
print(maxSubsetSum(nums))