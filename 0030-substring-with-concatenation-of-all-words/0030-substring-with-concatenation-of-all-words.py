class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_length = len(words[0])
        window_length, target, ans = word_length * len(words), Counter(words), []
        for i in range(len(s) - window_length + 1):
            tmp = {}
            for j in range(i, i + window_length, word_length):
                word = s[j: j + word_length]
                if word not in target: break
                tmp[word] = tmp.get(word, 0) + 1
                if tmp[word] > target[word]: break
            else:
                if tmp == target: ans.append(i)
        return ans


        