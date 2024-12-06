class FenwickTree:
    def __init__(self, size, value):
        self.size = size
        self.ft = [value] * size

    def __lowbit(self, index):
        return index & -index

    def update(self, index, delta):
        while index < self.size:
            self.ft[index] += delta
            index += self.__lowbit(index)

    def query(self, index):
        ans = 0
        while index:
            ans += self.ft[index]
            index -= self.__lowbit(index)
        return ans


class NumArray:

    def __init__(self, nums: List[int]):
        self.ft = FenwickTree(len(nums) + 1, 0)
        self.nums = nums
        for i, num in enumerate(nums):
            self.ft.update(i + 1, num)

        

    def update(self, index: int, val: int) -> None:
        self.ft.update(index + 1, val - self.nums[index])
        self.nums[index] = val

        

    def sumRange(self, left: int, right: int) -> int:
        return  self.ft.query(right + 1) - self.ft.query(left)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)