def quickSort(nums: list) -> list:
    if len(nums) in (0, 1):
        return nums

    p = nums[-1]
    l = [x for x in nums[:-1] if x <= p]
    r = [x for x in nums[:-1] if x > p]

    return quickSort(l) + [p] + quickSort(r)


# Run example
nums = [5, 8, 2, 4, 1, 0]
print(quickSort(nums))


# Run result
# [0, 1, 2, 4, 5, 8]
