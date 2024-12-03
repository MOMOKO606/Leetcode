class Solution:
    def nthUglyNumber(self, n: int) -> int:
        min_heap, visited = [1], set([1])
        while n:
            ans, n = heapq.heappop(min_heap), n - 1
            if ans * 2 not in visited:
                heapq.heappush(min_heap, ans * 2)
                visited.add(ans * 2)
            if ans * 3 not in visited:
                heapq.heappush(min_heap, ans * 3)
                visited.add(ans * 3)
            if ans * 5 not in visited:
                heapq.heappush(min_heap, ans * 5)
                visited.add(ans * 5)
        return ans

        