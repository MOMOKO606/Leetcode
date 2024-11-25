class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack, ans, cur_time = [], [0] * n, 0
        for log in logs:
            id, hint, time = log.split(":")
            id = int(id)
            time = int(time)
            if hint == "start":
                if stack: 
                    ans[stack[-1]] += time - cur_time
                stack.append(id)    
                cur_time = time
            else:
                ans[stack.pop()] += time - cur_time + 1
                cur_time = time + 1
        return ans
        