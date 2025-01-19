class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available, used, holds = [i for i in range(n)], [], [0] * n
        for start, end in meetings:
            while used and used[0][0] <= start:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)
            
            if not available:
                new_end, room = heapq.heappop(used)
                end = new_end + end - start
                heapq.heappush(available, room)
            
            room = heapq.heappop(available)
            holds[room] += 1
            heapq.heappush(used, (end, room))
        
        return holds.index(max(holds))

        