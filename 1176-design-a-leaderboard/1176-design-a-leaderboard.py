class Leaderboard:

    def __init__(self):
        self.id_2_score = collections.defaultdict(int)
        

    def addScore(self, playerId: int, score: int) -> None:
        self.id_2_score[playerId] += score
        
        

    def top(self, K: int) -> int:
        min_heap = []
        for score in self.id_2_score.values():
            heapq.heappush(min_heap, score)
            if len(min_heap) == K + 1:
                heapq.heappop(min_heap)
        return sum(min_heap)
        

    def reset(self, playerId: int) -> None:
        self.id_2_score[playerId] = 0
        
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)