class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)
        self.k = k
        

    def add(self, val: int) -> int:
        bisect.insort(self.nums, val)
        return self.nums[-self.k]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)