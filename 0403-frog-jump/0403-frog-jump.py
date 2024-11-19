class Solution:
    def canCross(self, stones: List[int]) -> bool:
        @cache
        def dfsHelper(pos, speed):
            if pos == target: return True
            if pos not in stones: return False
            for s in [speed - 1, speed, speed + 1]:
                if s > 0:
                    if dfsHelper(pos + s, s): return True
            return False
        
        target, stones = stones[-1], set(stones)
        return dfsHelper(0, 0)


            
        