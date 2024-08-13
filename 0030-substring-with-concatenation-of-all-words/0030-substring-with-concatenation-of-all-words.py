class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_length, target, ans = len(words[0]), Counter(words), []
        window_length = word_length * len(words)
        for i in range(len(s) - window_length + 1):
            tmp = {}
            for j in range(i, i + window_length, word_length):
                new_word = s[j: j + word_length]
                if new_word not in target: 
                    break
                else:
                    tmp[new_word] = tmp.get(new_word, 0) + 1
            else:
                if tmp == target: ans.append(i)
        return ans

        