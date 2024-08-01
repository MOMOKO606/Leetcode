class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        window_length, word_length, target, ans = len(words) * len(words[0]), len(words[0]), Counter(words), []
        for i in range(len(s) - window_length + 1):
            cur_words = {}
            for j in range(i, i + window_length, word_length):
                cur_word = s[j: j + word_length]
                if cur_word not in target: break
                cur_words[cur_word] = cur_words.get(cur_word, 0) + 1
                if cur_words[cur_word] > target[cur_word]: break
            else:
                if target == cur_words: ans.append(i)
        return ans

        