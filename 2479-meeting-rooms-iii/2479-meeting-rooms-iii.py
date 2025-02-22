class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        room_heap, schedule_heap, meetings, freqs, largest_freq, ans = [i for i in range(n)], [], sorted(meetings), [0] * n, -inf, 0
        for start, end in meetings:
            while schedule_heap and start >= schedule_heap[0][0]:
                _, room_id = heapq.heappop(schedule_heap)
                heapq.heappush(room_heap, room_id)
            
            if not room_heap:
                cur_end, room_id = heapq.heappop(schedule_heap)
                end = cur_end + end - start
                heapq.heappush(room_heap, room_id) 

            room_id = heapq.heappop(room_heap)
            heapq.heappush(schedule_heap, [end, room_id])
            freqs[room_id] += 1
        
        for i in range(len(freqs) - 1, -1, -1):
            if freqs[i] >= largest_freq:
                largest_freq, ans = freqs[i], i
        return ans


        