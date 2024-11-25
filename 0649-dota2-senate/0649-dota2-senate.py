class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n, radiant, dire = len(senate), [], []
        for i, senator in enumerate(senate):
            if senator == "R":
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant.pop(0) + n)
                dire.pop(0)
            else:
                dire.append(dire.pop(0) + n)
                radiant.pop(0)
        return "Radiant" if radiant else "Dire"