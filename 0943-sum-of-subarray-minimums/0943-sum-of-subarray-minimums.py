class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack, ans, arr = [], 0, [-inf] + arr + [-inf]
        for j, num in enumerate(arr):
            while stack and num < arr[stack[-1]]:
                k = stack.pop()
                ans += (k - stack[-1]) * (j - k) * arr[k]
            stack.append(j)
        return ans % (10 ** 9 + 7)         