def selectionSort(nums: list) -> list:
    for i in range(len(nums) - 1):
        minNum = nums[i:].index(min(nums[i:]))
        nums[i], nums[i + minNum] = nums[i + minNum], nums[i]

    return nums


# Run example
nums = [5, 8, 2, 4, 1, 0]
print(selectionSort(nums))


# Run result
# [0, 1, 2, 4, 5, 8]
