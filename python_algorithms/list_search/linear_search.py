example_list = [5, 2, 10, 1, 18, 3, 7, 4]
target = 8


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


print(linear_search(example_list, target))
