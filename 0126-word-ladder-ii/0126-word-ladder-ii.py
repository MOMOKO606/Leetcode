class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def printPaths(word=endWord, seq=[]):
            if word == beginWord:
                ans.append([word] + seq)
                return
            if word not in paths: return
            for neighbor in paths[word]:
                printPaths(neighbor, [word] + seq)


        wordList = set(wordList)
        if endWord not in wordList: return []
        if beginWord in wordList: wordList.remove(beginWord)
        queue, paths, ans = [beginWord], {}, []
        while queue:
            localVisited = set()
            for word in queue:
                for i in range(len(word)):
                    for char in "abcdefghijklmnopqrstuvwxyz":
                        newWord = word[:i] + char + word[i + 1:]
                        if newWord in wordList:
                            localVisited.add(newWord)
                            paths[newWord] = paths.get(newWord, []) + [word]
            for word in localVisited:
                wordList.remove(word)
            queue = list(localVisited)
       
        printPaths()
        return ans