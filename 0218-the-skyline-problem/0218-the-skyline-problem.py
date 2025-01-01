class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        sweepline, min_heap, ans = [], [0], []
        for left, right, height in buildings:
            sweepline.append([left, -height])
            sweepline.append([right, height])

        for pos, height in sorted(sweepline):
            if height < 0:
                if height < min_heap[0]:
                    ans.append([pos, -height])
                heapq.heappush(min_heap, height)
            else:
                min_heap.remove(-height)
                heapq.heapify(min_heap)
                if height > -min_heap[0]:
                    ans.append([pos, -min_heap[0]])
        return ans



        