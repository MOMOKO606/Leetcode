class SmallestInfiniteSet:

    def __init__(self):
        self.poped = set()
        self.cur_num = 1
        

    def popSmallest(self) -> int:
        while self.cur_num in self.poped:
            self.cur_num += 1
        self.poped.add(self.cur_num)
        return self.cur_num
        

    def addBack(self, num: int) -> None:
        if num in self.poped:
            self.poped.remove(num)
        if num < self.cur_num:
            self.cur_num = num
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)