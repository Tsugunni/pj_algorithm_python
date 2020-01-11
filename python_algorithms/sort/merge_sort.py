def merge(left, right):
    n = len(left + right)
    s = max(left + right) + 1

    left.append(s)
    right.append(s)

    a = []
    while len(a) < n:
        a.append(left.pop(0)) if left[0] <= right[0] else a.append(right.pop(0))

    return a

def mergeSort(nums: list) -> list:
    if len(nums) == 1:
        return nums

    mid = len(nums) // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])

    return merge(left, right)