class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        def dfs_helper(i):
            while i < len(nums) and not nums[i]:
                i += 1
            if i == len(accounts): return 0
            ans = inf
            for j in range(i + 1, len(accounts)):
                if nums[i] * nums[j] < 0:
                    nums[j] += nums[i]
                    ans = min(ans, 1 + dfs_helper(i + 1))
                    nums[j] -= nums[i]
            return ans

        accounts = collections.defaultdict(int)
        for u, v, w in transactions:
            accounts[v] += w
            accounts[u] -= w

        nums = list(accounts.values())
        return dfs_helper(0)

        