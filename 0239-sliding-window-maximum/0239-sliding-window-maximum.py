class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque, ans = collections.deque([]), []
        for j, num in enumerate(nums):
            if deque and j - deque[0] >= k:
                deque.popleft()
            while deque and num > nums[deque[-1]]:
                deque.pop()
            deque.append(j)
            if j >= k - 1: ans.append(nums[deque[0]])
        return ans


        