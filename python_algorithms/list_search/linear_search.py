def linear_search(nums: list, taget: int) -> int:
    result = 0
    index = 0
    for x in range(0, len(nums)):
        if nums[x] == target:
            result = 1
            index = x
            break
    if result == 1:
        return index
