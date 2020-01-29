def insertionSort(nums: list) -> list:
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] >= nums[j - 1]:
                break
            else:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]

    return nums