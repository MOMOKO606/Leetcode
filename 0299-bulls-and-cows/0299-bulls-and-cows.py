class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows, targets, indexes = 0, 0, {}, []
        for i, (char1, char2) in enumerate(zip(secret, guess)):
            if char1 == char2: bulls += 1
            else: targets[char1], indexes = targets.get(char1, 0) + 1, indexes + [i]

        for i in indexes:
            if guess[i] in targets and targets[guess[i]] > 0:
                cows, targets[guess[i]] = cows + 1, targets[guess[i]] - 1
        return str(bulls) + "A" + str(cows) + "B"

        
        