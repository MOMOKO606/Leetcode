class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # We use a maxHeap to store all the height we have sweeped, and
        # Maintain the current highest building at top.
        # So we initialize the maxHeap with height 0
        heap = [0]
        # We use sweepLines to go over the whole pic from left to right
        # Make the height negative to represent we entry a building from the left,
        # Make the height to remain positive to represent we leave a building from the right.
        # Reason: cover the edge cases.
        #        - 1. If many buildings have the same left points but different height, we should only 
        #             draw the heighest one.
        #        - 2. If many buildings have the same right points but different height, we should only 
        #             draw the lowest one.
        # So after sorting the sweepLines, the x-coordinate will be sorted first, 
        # then the highest height when entering, the lowest when leaving
        sweepLines = []
        for left, right, height in buildings:
            sweepLines.append([left, -height])
            sweepLines.append([right, height])
        sweepLines.sort()

        # Now let's sweep the whole pic
        ans = []
        for endPoint, height in sweepLines:
            # If we are entering the building
            if height < 0:
                # If we have a higher building now, add it to the ans
                if height < heap[0]:
                    ans.append([endPoint, -height])
                # Remember to keep tracking of all the heights when we enter buildings.
                heapq.heappush(heap, height)
            # If we are leaving the building
            else:
                heap.remove(-height)
                heapq.heapify(heap)
                # If we have a lower building now, add it to the ans
                if -height < heap[0]:
                    ans.append([endPoint, -heap[0]])
        return ans

                