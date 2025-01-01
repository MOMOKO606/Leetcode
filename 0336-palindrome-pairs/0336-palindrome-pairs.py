class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        indexes, ans = {word: i for i, word in enumerate(words)}, set()
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                left = word[j:][::-1]
                if left in indexes and (indexes[left], i) not in ans and indexes[left] != i and left + word == (left + word)[::-1]:
                    ans.add((indexes[left], i))
            for j in range(len(word) + 1):
                right = word[:j][::-1]
                if right in indexes and (i, indexes[right]) not in ans and i != indexes[right] and word + right == (word + right)[::-1]:
                    ans.add((i, indexes[right]))
        return list(map(list, ans))
            

        