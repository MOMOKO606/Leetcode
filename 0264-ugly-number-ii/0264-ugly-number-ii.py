class Solution:
    def nthUglyNumber(self, n: int) -> int:
        minHeap, nums, seen = [1], [], {1,}
        for _ in range(1690):
            num = heapq.heappop(minHeap)
            nums.append(num)
            for factor in [2, 3, 5]:
                tmp = factor * num
                if tmp not in seen:
                    heapq.heappush(minHeap, tmp)
                    seen.add(tmp)
        return nums[n - 1]

        