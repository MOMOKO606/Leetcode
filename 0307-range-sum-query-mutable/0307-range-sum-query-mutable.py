class FenwickTree:
    def __init__(self, size, value):
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


class NumArray:

    def __init__(self, nums: List[int]):
        self.trans = {num: i + 1 for i, num in enumerate(sorted(nums))}
        self.nums = nums
        ft = FenwickTree(len(nums) + 1, 0)
        for num in nums:
            k = self.trans[num]
            ft.update(k, num)
        self.ft = ft

        

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.ft.update(index + 1, delta)

        

    def sumRange(self, left: int, right: int) -> int:
        return self.ft.query(right + 1) - self.ft.query(left)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)