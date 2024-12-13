class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, ans = [], [0] * len(temperatures)
        for j, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                i = stack.pop()
                ans[i] = j - i
            stack.append(j)
        return ans

        