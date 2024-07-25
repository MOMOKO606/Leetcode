class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows, secret, guess = 0, 0, list(secret), list(guess)
        for i in range(len(secret)): 
            if secret[i] == guess[i]:
                bulls += 1
                secret[i], guess[i] = "#", "#"
        count = Counter(secret)
        for char, freq in Counter(guess).items():
            if char == "#" or char not in count: continue
            cows += min(freq, count[char])
        return f"{bulls}A{cows}B"

            
        