class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        target, ans = Counter(chars), 0
        for word in words:
            char_len = 0
            for char, freq in Counter(word).items():
                if char not in target or target[char] < freq: break
                char_len += freq
            else:
                ans += char_len
        return ans

        
        