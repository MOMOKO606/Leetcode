class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        alice, bob = 0, 0
        for i, num in enumerate(possible):
            if not num: possible[i] = -1
            bob += possible[i]

        for i in range(len(possible) - 1):
            alice += possible[i]
            bob -= possible[i]
            if alice > bob: return i + 1
        return -1

        
        