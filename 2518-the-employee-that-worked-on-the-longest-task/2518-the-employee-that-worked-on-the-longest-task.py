class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        tasks, start, ans = [], 0, 0
        for id, end in logs:
            tasks.append([end - start, id])
            start = end 
        return max(tasks, key=lambda x: (x[0], -x[1]))[1]
