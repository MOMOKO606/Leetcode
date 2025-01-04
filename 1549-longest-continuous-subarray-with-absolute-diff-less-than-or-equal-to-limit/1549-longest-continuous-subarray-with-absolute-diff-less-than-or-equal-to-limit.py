from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_window, min_window, ans, i = deque([]), deque([]), 0, -1
        for j in range(len(nums)):
            while max_window and max_window[-1][0] < nums[j]:
                max_window.pop()
            max_window.append([nums[j], j])
            while min_window and min_window[-1][0] > nums[j]:
                min_window.pop()
            min_window.append([nums[j], j])
            while max_window[0][0] - min_window[0][0] > limit:
                i += 1
                while i >= max_window[0][1]:
                    max_window.popleft()
                while i >= min_window[0][1]:
                    min_window.popleft() 
            ans = max(ans, j - i)
        return ans



        