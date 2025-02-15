class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def printPaths(word=endWord, seq=[]):
            if word == beginWord:
                seq = [word] + seq
                ans.append(seq[:])
                return
            for neighbor in paths[word]:
                printPaths(neighbor, [word] + seq)

        wordList, ans = set(wordList), []
        if endWord not in wordList: return []
        if beginWord in wordList: wordList.remove(beginWord)
        queue, paths = [beginWord], {}
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
                if word == endWord:
                    printPaths()
                    return ans
            queue = list(localVisited)
        return []

        
        


        