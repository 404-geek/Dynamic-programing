def merge(nums1, m: int, nums2, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """

    i = 0
    j = 0
    res = []

    while i < m and j < n:

        if nums1[i] < nums2[j]:

            res.append(nums1[i])
            i += 1

        else:
            res.append(nums2[j])
            j += 1

    if i != m:
        res.extend(nums1[i:])
    if j != n:
        res.extend(nums2[j:])

    return res

print(merge([1,2,3,0,0,0],3,[2,5,6], 3))