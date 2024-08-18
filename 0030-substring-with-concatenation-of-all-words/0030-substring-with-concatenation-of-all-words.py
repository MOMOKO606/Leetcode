class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_length = len(words[0])
        window_length, target, ans = len(words) * word_length, Counter(words), []
        for i in range(len(s) - window_length + 1):
            cur = {}
            for j in range(i, i + window_length, word_length):
                word = s[j: j + word_length] 
                if word not in target: break
                cur[word] = cur.get(word, 0) + 1
            else:
                if cur == target: ans.append(i)
        return ans


        