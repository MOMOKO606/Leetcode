class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1, version2 = version1.split("."), version2.split(".")
        l = max(len(version1), len(version2))
        for _ in range(l - len(version1)): version1.append("0")
        for _ in range(l - len(version2)): version2.append("0")


        for v1, v2 in zip(version1, version2):
            v1, v2 = int(v1), int(v2)
            if v1 > v2: return 1
            elif v1 < v2: return -1
        else: return 0
        