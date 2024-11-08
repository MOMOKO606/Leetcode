class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1, version2 = list(map(int, version1.split("."))), list(map(int, version2.split(".")))
        m, n = len(version1), len(version2)
        if m < n: version1 += [0] * (n - m)
        if n < m: version2 += [0] * (m - n)
        for v1, v2 in zip(version1, version2):
            if v1 > v2: return 1
            elif v1 < v2: return -1
        return 0
        