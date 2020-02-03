def bubbleSort(nums: list) -> list:
    for i in range(len(nums)):
        for j in range(len(nums) - 1, i, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]

    return nums


# Run example
nums = [5, 8, 2, 4, 1, 0]
print(bubbleSort(nums))


# Run result
# [0, 1, 2, 4, 5, 8]
