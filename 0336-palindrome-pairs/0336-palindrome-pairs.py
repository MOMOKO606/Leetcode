class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        indexes, ans = {word: i for i, word in enumerate(words)}, set()
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                left, right = word[:j], word[j:]
                if right[::-1] in indexes and indexes[right[::-1]] != i and left == left[::-1]:
                    ans.add((indexes[right[::-1]], i))
                if left[::-1] in indexes and i != indexes[left[::-1]] and right == right[::-1]:
                    ans.add((i, indexes[left[::-1]]))
        return list(ans)
            

        