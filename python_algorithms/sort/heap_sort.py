# pattern1 (use library)
from heapq import heappush
from heapq import heappop


def linked_heap_sort(nums: list) -> list:
    heap = []
    while nums:
        heappush(heap, nums.pop())
    while heap:
        nums.append(heappop(heap))

    return nums



# pattern2
def heap_sort(nums: list) -> list:
    heapify(nums)
    index = len(nums) - 1
    while index:
        nums[0], nums[index] = nums[index], nums[0]
        _siftup(nums, 0, index)
        index = index - 1

    nums.reverse()
    return nums


def _siftdown(heap: list, startpos: int, pos: int):
    newitem = heap[pos]
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem


def _siftup(heap: list, pos: int, endpos: int):
    startpos = pos
    newitem = heap[pos]
    childpos = 2 * pos + 1
    while childpos < endpos:
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2 * pos + 1
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)


def heapify(x: list):
    n = len(x)
    for i in reversed(range(n // 2)):
        _siftup(x, i, n)


# Run example
nums = [5, 8, 2, 4, 1, 0]
print(linked_heap_sort(nums))
print(heap_sort(nums))


# Run result
# [0, 1, 2, 4, 5, 8]
