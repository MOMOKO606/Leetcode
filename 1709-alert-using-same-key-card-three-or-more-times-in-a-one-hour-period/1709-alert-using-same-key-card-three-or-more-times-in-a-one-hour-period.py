class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        logs, ans = collections.defaultdict(list), []
        for name, time in zip(keyName, keyTime):
            time = int(time[:2]) * 60 + int(time[3:])
            bisect.insort(logs[name], time)
        
        for name, times in logs.items():
            for i in range(len(times) - 2):
                if i + 2 < len(times) and times[i + 2] - times[i] <= 60:
                    ans.append(name)
                    break
        return sorted(ans)
            

        