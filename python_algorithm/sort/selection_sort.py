from typing import List


def sSort(nums: List[int]) -> List[int]:
    for i in range(len(nums) - 1):
        minNum = nums[i:].index(min(nums[i:]))
        nums[i], nums[i + minNum] = nums[i + minNum], nums[i]

    return nums


print(sSort([5, 2, 6, 1, 6, 0]))
