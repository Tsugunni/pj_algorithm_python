def linear_search(nums: list, target: int) -> int:
    result = 0
    index = 0
    for x in range(0, len(nums)):
        if nums[x] == target:
            result = 1
            index = x
            break
    if result == 1:
        return index


# Run example
my_list = [1, 3, 5, 7, 9]
print(linear_search(my_list, 9))


# Run result
# 4
