class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans, stack = [0] * n, []
        for log in logs:
            log = log.split(":")
            id, sign, time = int(log[0]), log[1], int(log[2])
            if sign == "start":
                if stack: ans[stack[-1][0]] += time - stack[-1][1]
                stack.append([id, time])
            else:
                ans[stack[-1][0]] += time - stack[-1][1] + 1
                stack.pop()
                if stack: stack[-1][1] = time + 1
        return ans

        