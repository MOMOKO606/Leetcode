class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        freqs, ans = collections.defaultdict(list), []
        for name, time in zip(keyName, keyTime):
            time = time.split(":")
            bisect.insort(freqs[name], int(time[0]) * 60 + int(time[1]))

        for name, times in freqs.items():
            for i in range(len(times) - 2):
                if times[i + 2] <= times[i] + 60:
                    ans.append(name)
                    break
        return sorted(ans)

        

        