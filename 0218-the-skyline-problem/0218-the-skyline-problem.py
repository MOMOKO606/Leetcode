class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        sweeplines, maxHeap, ans = [], [0], []
        for left, right, height in buildings:
            sweeplines.append([left, -height])
            sweeplines.append([right, height])
        sweeplines.sort()

        for pos, height in sweeplines:
            if height < 0:
                if height < maxHeap[0]:
                    ans.append([pos, -height])
                heapq.heappush(maxHeap, height)
            else:
                maxHeap.remove(-height)
                heapq.heapify(maxHeap)
                if height > -maxHeap[0]:
                    ans.append([pos, -maxHeap[0]])
        return ans

                

        