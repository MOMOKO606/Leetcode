class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        deltas = [heights[i] - heights[i - 1] for i in range(1, len(heights))]

        max_heap = []
        for h in deltas:
            if h > 0: heapq.heappush(max_heap, -h)

        for i, h in enumerate(deltas):
            if h <= 0: continue
            if h == -max_heap[0] and ladders:
                ladders -= 1
                heapq.heappop(max_heap)
            elif bricks >= h:
                bricks -= h
            elif ladders:
                ladders -= 1
            else:
                return i
        return len(deltas)

            

        