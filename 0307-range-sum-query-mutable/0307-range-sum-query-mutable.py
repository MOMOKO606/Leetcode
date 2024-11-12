class FenwickTree:
    def __init__(self, size, value):
        self.ft = [value] * size
        self.size = size

    def __lowbit(self, i):
        return i & -i

    def update(self, i, delta):
        while i < self.size:
            self.ft[i] += delta
            i += self.__lowbit(i)

    def query(self, i):
        ans = 0
        while i:
            ans += self.ft[i]
            i -= self.__lowbit(i)
        return ans


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.ft = FenwickTree(len(nums) + 1, 0)
        for i, num in enumerate(nums):
            self.ft.update(i + 1, num)
        

    def update(self, index: int, val: int) -> None:
        self.ft.update(index + 1, val - self.nums[index])
        self.nums[index] = val
        

    def sumRange(self, left: int, right: int) -> int:
        return self.ft.query(right + 1) - self.ft.query(left)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)