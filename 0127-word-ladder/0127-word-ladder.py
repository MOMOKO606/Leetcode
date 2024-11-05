class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList: return 0
        queue, ans = [beginWord], 1
        while queue:
            nextQueue = []
            for word in queue:
                if word == endWord: return ans
                for i in range(len(word)):
                    for char in "abcdefghijklmnopqrstuvwxyz":
                        newWord = word[:i] + char + word[i + 1:]
                        if newWord in wordList:
                            wordList.remove(newWord)
                            nextQueue.append(newWord)
            queue, ans = nextQueue, ans + 1
        return 0


        