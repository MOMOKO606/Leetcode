class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        visited, ans = {}, []
        for name, time in zip(keyName, keyTime):
            hours, mins = time.split(":")
            visited[name] = visited.get(name, []) + [int(hours) * 60 + int(mins)]
        
        for name, times in visited.items():
            times.sort()
            for i in range(len(times) - 2):
                if times[i + 2] - times[i] <= 60:
                    ans.append(name)
                    break
        return sorted(ans)
