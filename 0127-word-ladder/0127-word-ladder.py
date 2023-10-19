class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue, steps, wordList = [beginWord], 1, set(wordList)
        while queue:
            nextQueue = []
            for word in queue:
                for i in range(len(word)):
                    for char in "abcdefghijklmnopqrstuvwxyz":
                        newWord = word[:i] + char + word[i + 1:]
                        if newWord not in wordList: continue
                        if newWord == endWord: return steps + 1
                        nextQueue.append(newWord)
                        wordList.remove(newWord)
            queue, steps = nextQueue, steps + 1
        return 0