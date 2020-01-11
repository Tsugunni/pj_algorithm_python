def sSort(nums: list) -> list:
    for i in range(len(nums) - 1):
        minNum = nums[i:].index(min(nums[i:]))
        nums[i], nums[i + minNum] = nums[i + minNum], nums[i]

    return nums
