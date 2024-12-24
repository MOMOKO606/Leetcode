class FenwickTree:
    def __init__(self, value, size):
        self.nums = [value] * size
        self.size = size

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
        ft = FenwickTree(0, len(nums) + 1)
        for i, num in enumerate(nums):
            ft.update(i + 1, num)
        self.ft, self.nums = ft, nums
        
        

    def update(self, index: int, val: int) -> None:
        self.ft.update(index + 1, val - self.nums[index])
        self.nums[index] = val
        


    def sumRange(self, left: int, right: int) -> int:
        return self.ft.query(right + 1) - self.ft.query(left)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)