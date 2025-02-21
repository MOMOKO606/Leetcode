class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        def dfs_helper(i=0):
            while i < len(nums) and not nums[i]:
                i += 1
            if i == len(nums): return 0
            ans = inf
            for j in range(i + 1, len(nums)):
                if nums[j] * nums[i] < 0:
                    nums[j] += nums[i]
                    ans = min(ans, 1 + dfs_helper(i + 1))
                    nums[j] -= nums[i]
            return ans


        # Build the graph
        accounts = collections.defaultdict(int)
        for u, v, w in transactions:
            accounts[u] -= w
            accounts[v] += w
        nums = list(accounts.values())
        return dfs_helper()
        