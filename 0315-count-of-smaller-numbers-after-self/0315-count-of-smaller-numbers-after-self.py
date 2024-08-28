class FenwickTree:
    def __init__(self, n, original_value):
        self.size = n
        self.tree = [original_value] * n

    def __lowbit(self, index):
        return index & -index

    def update(self, index, delta):
        while index < self.size:
            self.tree[index] += delta
            index += self.__lowbit(index)


    def query(self, index):
        ans = 0
        while index:
            ans += self.tree[index]
            index -= self.__lowbit(index)
        return ans



class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        indices = {num: i + 1 for i, num in enumerate(sorted(set(nums)))}
        ft = FenwickTree(len(indices) + 1, 0) 
        ans = []
        for num in reversed(nums):
            index = indices[num]
            ft.update(index, 1)
            ans.append(ft.query(index - 1))
        return ans[::-1]


        