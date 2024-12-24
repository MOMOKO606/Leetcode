class FenwickTree:
    def __init__(self, value, size):
        self.size = size
        self.nums = [value] * size

    def lowbit(self, index):
        return index & -index

    def update(self, index, delta):
        while index < self.size:
            self.nums[index] += delta
            index += self.lowbit(index)


    def query(self, index):
        ans = 0
        while index:
            ans += self.nums[index]
            index -= self.lowbit(index)
        return ans
        

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        trans = {num: i + 1 for i, num in enumerate(sorted(list(set(nums))))}
        ft, ans = FenwickTree(0, len(trans) + 1), []
        for num in reversed(nums):
            k = trans[num]
            ft.update(k, 1)
            ans.append(ft.query(k - 1))
        return ans[::-1]

        