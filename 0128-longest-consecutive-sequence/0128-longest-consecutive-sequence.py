class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def parent(i):
            root = i
            while p[root] != root:
                root = p[root]
            while p[i] != i:
                p[i], i = root, p[i]
            return root

        def connect(i, j):
            pi, pj = parent(i), parent(j)
            p[pi] = pj

        if not nums: return 0
        p, numSet = {num: num for num in nums}, set(nums)
        for num in numSet:
            if num - 1 in numSet: connect(num, num - 1)
            if num + 1 in numSet: connect(num, num + 1)
        
        roots = {}
        for num in numSet:
            pnum = parent(num)
            roots[pnum] = roots.get(pnum, 0) + 1
        return max(roots.values())


        