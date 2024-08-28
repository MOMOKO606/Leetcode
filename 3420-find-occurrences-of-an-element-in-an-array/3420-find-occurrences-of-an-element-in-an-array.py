class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:   
        count, check, ans = 1, {}, []
        for i, num in enumerate(nums):
            if num == x:
                check[count] = i
                count += 1

        for query in queries:
            if query in check:
                ans.append(check[query])
            else:
                ans.append(-1)
        return ans

        