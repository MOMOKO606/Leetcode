class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def parent(i):
            root = i
            while root != p[root]:
                root = p[root]
            while root != p[i]:
                temp = p[i]
                p[i] = root
                i = temp
            return root

        def connect(i, j):
            pi, pj = parent(i), parent(j)
            p[pi] = pj
        if not nums: return 0        
        p, roots = {}, {}
        for num in nums:
            p[num] = num
        for num in nums:
            if num - 1 in p: connect(num, num - 1)
            if num + 1 in p: connect(num, num + 1)
        for key in p.keys():
            pkey = parent(key)
            roots[pkey] = roots.get(pkey, 0) + 1
        return max(roots.values())
        
