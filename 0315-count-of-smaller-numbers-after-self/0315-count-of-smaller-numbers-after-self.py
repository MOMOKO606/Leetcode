class FenwickTree:
    def __init__(self, original_value, size):
        self.ft = [original_value] * size

    def __lowbit(self, i):
        return i & -i

    def update(self, i, delta):
        while i < len(self.ft):
            self.ft[i] += delta
            i += self.__lowbit(i)

    def query(self, i):
        ans = 0
        while i > 0:
            ans += self.ft[i]
            i -= self.__lowbit(i)
        return ans


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        transfer, ans = {num: i + 1 for i, num in enumerate(sorted(set(nums)))}, []
        ft = FenwickTree(original_value=0, size=len(transfer) + 1)
        for num in reversed(nums):
            i = transfer[num]
            ft.update(i, 1)
            ans.append(ft.query(i - 1))
        return ans[::-1]

       

        