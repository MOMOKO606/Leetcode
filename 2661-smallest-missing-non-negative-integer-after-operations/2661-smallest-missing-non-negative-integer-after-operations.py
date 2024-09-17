class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        visited = collections.defaultdict(int)
        for num in nums:
            visited[num % value] += 1
    
        ans = 0
        while ans % value  in visited and visited[ans % value] > 0:
            visited[ans % value] -= 1
            ans += 1
        return ans
        