class Solution:
    def nthUglyNumber(self, n: int) -> int:
        minHeap, generated = [1], set()
        for _ in range(n):
            cur_num = heapq.heappop(minHeap)
            for prime in [2, 3, 5]:
                potential = prime * cur_num
                if potential not in generated:
                    heapq.heappush(minHeap, potential)
                    generated.add(potential)
        return cur_num

        