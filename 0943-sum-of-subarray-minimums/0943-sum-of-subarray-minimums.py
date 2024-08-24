class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr, ans, stack, MOD = [-inf] + arr + [-inf], 0, [], 10 ** 9 + 7 
        for j, num in enumerate(arr):
            while stack and num < arr[stack[-1]]:
                k = stack.pop()
                ans += (k - stack[-1]) * (j - k) * arr[k]
            stack.append(j)
        return ans % MOD

        