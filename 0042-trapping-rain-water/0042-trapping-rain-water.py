class Solution:
    def trap(self, height: List[int]) -> int:
        stack, ans = [], 0
        for j, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                k = stack.pop()
                if stack: 
                    i = stack[-1]
                    ans += max(0, min(h, height[i]) - height[k]) * (j - i - 1)
            stack.append(j)
        return ans


        