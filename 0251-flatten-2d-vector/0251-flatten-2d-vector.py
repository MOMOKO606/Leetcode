class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.i, self.j, self.vec = 0, 0, vec

        

    def next(self) -> int:
        if self.hasNext():
            ans = self.vec[self.i][self.j]
            self.j += 1
            return ans

        

    def hasNext(self) -> bool:
        while self.i < len(self.vec):
            if self.j < len(self.vec[self.i]): return True
            self.i, self.j = self.i + 1, 0
        return False
        
        
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()