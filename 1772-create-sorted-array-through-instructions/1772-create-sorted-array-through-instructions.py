class FenwickTree:
    def __init__(self, value, size):
        self.size = size
        self.ft = [value] * size

    def lowbit(self, index):
        return index & -index

    def update(self, i, delta):
        while i < self.size:
            self.ft[i] += delta
            i += self.lowbit(i)
    
    def query(self, i):
        ans = 0
        while i:
            ans += self.ft[i]
            i -= self.lowbit(i)
        return ans


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        trans = {num: i + 1 for i, num in enumerate(sorted(list(set(instructions))))}
        ft, ans = FenwickTree(0, len(trans) + 1), 0
        for i, num in enumerate(instructions):
            k = trans[num]
            ft.update(k, 1)
            ans += min(ft.query(k - 1), i + 1 - ft.query(k))
        return ans % (10 ** 9 + 7)


        