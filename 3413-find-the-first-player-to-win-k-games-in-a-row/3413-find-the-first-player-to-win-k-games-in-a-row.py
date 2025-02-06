class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        if k >= len(skills): return skills.index(max(skills))
        queue, count = collections.deque([(skill, i) for i, skill in enumerate(skills)]), 0
        while True:
            if queue[0][0] > queue[1][0]: queue[0], queue[1], count = queue[1], queue[0], count + 1
            else: count = 1
            queue.append(queue.popleft())
            if count == k: return queue[0][1]


        