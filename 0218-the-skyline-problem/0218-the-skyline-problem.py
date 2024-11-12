class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ans, maxHeap, sweepLines = [], [0], []
        for left, right, height in buildings:
            sweepLines.append([left, -height])
            sweepLines.append([right, height])
        sweepLines = sorted(sweepLines)

        for sweepLine in sweepLines:
            curEnd, curHeight = sweepLine[0], sweepLine[1]
            # Enter a building
            if curHeight < 0:
                if curHeight < maxHeap[0]:
                    ans.append([curEnd, -curHeight])
                heapq.heappush(maxHeap, curHeight)
            # Leaving a building
            else:
                maxHeap.remove(-curHeight)
                heapq.heapify(maxHeap)
                if curHeight > -maxHeap[0]:
                    ans.append([curEnd, -maxHeap[0]])
        return ans




        