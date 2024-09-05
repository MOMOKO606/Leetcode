class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue, count, wordList = [beginWord], 1, set(wordList)
        if beginWord in wordList: wordList.remove(beginWord)
        while queue:
            nextQueue = []
            for word in queue:
                for i in range(len(word)):
                    for char in "abcdefghijklmnopqrstuvwxyz":
                        newWord = word[:i] + char + word[i + 1:]
                        if newWord in wordList:
                            if newWord == endWord: return count + 1
                            wordList.remove(newWord)
                            nextQueue.append(newWord)
            queue, count = nextQueue, count + 1
        return 0

        