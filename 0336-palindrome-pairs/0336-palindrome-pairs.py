class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        words_set, visited, ans = {word: i for i, word in enumerate(words)}, set([]), []
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                left, right = word[:j], word[j:]
                if right == right[::-1] and left[::-1] in words_set and i != words_set[left[::-1]] and (i, words_set[left[::-1]]) not in visited:
                    visited.add((i, words_set[left[::-1]]))
                    ans.append([i, words_set[left[::-1]]])
                if left == left[::-1] and right[::-1] in words_set and i != words_set[right[::-1]] and (words_set[right[::-1]], i) not in visited:
                    visited.add((words_set[right[::-1]], i))
                    ans.append([words_set[right[::-1]], i])
        return ans

        