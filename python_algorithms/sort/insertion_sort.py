def insertionSort(nums: list) -> list:
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] >= nums[j - 1]:
                break
            else:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]

    return nums


# Run example
nums = [5, 8, 2, 4, 1, 0]
print(insertionSort(nums))


# Run result
# [0, 1, 2, 4, 5, 8]
