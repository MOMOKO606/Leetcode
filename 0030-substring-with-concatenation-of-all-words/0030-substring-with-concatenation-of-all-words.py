class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans, word_length, window_length, target = [], len(words[0]), len(words) * len(words[0]), Counter(words)
        for i in range(len(s) - window_length + 1):
            seen = collections.defaultdict(int)
            for j in range(i, i + window_length, word_length):
                word = s[j: j + word_length]
                seen[word] += 1
                if word not in target or seen[word] > target[word]: break
            else:
                ans.append(i)
        return ans 

        