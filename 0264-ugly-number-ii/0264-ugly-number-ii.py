class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums, min_heap, seen = [], [1], set([1])
        for _ in range(n):
            nums.append(heapq.heappop(min_heap))
            for factor in [2, 3, 5]:
                node = nums[-1] * factor
                if node not in seen:
                    heapq.heappush(min_heap, node)
                    seen.add(node)
        return nums[-1]

        