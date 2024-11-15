class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans, visited = [], Counter(nums1)
        for num in nums2:
            if num in visited and visited[num] > 0:
                ans.append(num)
                visited[num] -= 1
        return ans
        
        