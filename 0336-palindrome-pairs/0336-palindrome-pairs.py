class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        visited, ans = {word: i for i, word in enumerate(words)}, set()
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                left, right = word[:j], word[j:]
                # head + word = palindrome
                if left == left[::-1] and right[::-1] in visited and visited[right[::-1]] != i:
                    ans.add((visited[right[::-1]], i))
                # word + tail = palindrome
                if right == right[::-1] and left[::-1] in visited and visited[left[::-1]] != i:
                    ans.add((i, visited[left[::-1]]))
        return list(ans)
         
        