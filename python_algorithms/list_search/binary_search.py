def binary_search(nums: list, target: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        midValue = nums[mid]
        if midValue == target:
            return mid
        if midValue > target:
            high = mid - 1
        else:
            low = mid + 1

    return None