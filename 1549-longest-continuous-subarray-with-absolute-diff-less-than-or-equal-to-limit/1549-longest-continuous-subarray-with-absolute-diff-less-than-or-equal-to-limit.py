class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        i, ans, max_window, min_window = -1, 1, [], []
        for j in range(len(nums)):
            while max_window and nums[j] > nums[max_window[-1]]:
                max_window.pop()
            max_window.append(j)

            while min_window and nums[j] < nums[min_window[-1]]:
                min_window.pop()
            min_window.append(j)

            while nums[max_window[0]] - nums[min_window[0]] > limit:
                i += 1
                while i >= max_window[0]:
                    max_window.pop(0)
                while i >= min_window[0]:
                    min_window.pop(0)            
            
            ans = max(ans, j - i)
        return ans


        