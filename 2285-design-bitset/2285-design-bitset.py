class Bitset:

    def __init__(self, size: int):
        self.bits = [0] * size
        self.size = size
        self.flipped = False
        self.ones = 0
        

    def fix(self, idx: int) -> None:
        if not self.flipped:
            if not self.bits[idx]: 
                self.bits[idx], self.ones = 1, self.ones + 1
        else:
            if self.bits[idx]: 
                self.bits[idx], self.ones = 0, self.ones + 1


    def unfix(self, idx: int) -> None:
        if not self.flipped:
            if self.bits[idx]:
                self.bits[idx], self.ones = 0, self.ones - 1
        else:
            if not self.bits[idx]:
                self.bits[idx], self.ones = 1, self.ones - 1
        

    def flip(self) -> None:
        self.flipped = not self.flipped
        self.ones = self.size - self.ones


    def all(self) -> bool:
        return self.ones == self.size
        

    def one(self) -> bool:
        return self.ones > 0
        

    def count(self) -> int:
        return self.ones
        

    def toString(self) -> str:
        if not self.flipped:
            return "".join(map(str, self.bits))
        else:
            ans = ""
            for bit in self.bits:
                if bit: ans += "0"
                else: ans += "1"
            return ans


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()