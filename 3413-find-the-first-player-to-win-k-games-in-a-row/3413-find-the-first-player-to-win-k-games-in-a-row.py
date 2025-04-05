class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        if k >= len(skills): return skills.index(max(skills))
        deque = collections.deque([(skill, i) for i, skill in enumerate(skills)])
        count= 0
        while count < k:
            if deque[0][0] > deque[1][0]:
                count += 1
                deque[0], deque[1] = deque[1], deque[0]     
            else:
                count = 1
            deque.append(deque.popleft())
        return deque[0][1]
        