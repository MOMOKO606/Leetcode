class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr, stack, ans = [-inf] + arr + [-inf], [0], 0
        for j, num in enumerate(arr):
            while num < arr[stack[-1]]:
                k = stack.pop()
                ans += (k - stack[-1]) * (j - k) * arr[k]
            stack.append(j)
        return ans % (10 ** 9 + 7)
