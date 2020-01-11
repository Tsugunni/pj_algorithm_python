from heapq import heappush
from heapq import heappop


def linked_heap_sort(nums: list) -> list:
    heap = []
    while nums:
        heappush(heap, nums.pop())
    while heap:
        nums.append(heappop(heap))

    return nums
