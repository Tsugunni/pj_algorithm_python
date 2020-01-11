def quickSort(nums: list) -> list:
    if len(nums) in (0, 1):
        return nums

    p = nums[-1]
    l = [x for x in nums[:-1] if x <= p]
    r = [x for x in nums[:-1] if x > p]

    return quickSort(l) + [p] + quickSort(r)