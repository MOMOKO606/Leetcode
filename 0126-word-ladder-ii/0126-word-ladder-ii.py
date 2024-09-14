class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def printPath(word, seq):
            if word == beginWord:
                seq = [beginWord] + seq
                self.ans.append(seq[:])
                return
            if word not in paths: return
            for neighbor in paths[word]:
                printPath(neighbor, [word] + seq)
            


        wordList = set(wordList)
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
            if endWord in localVisited: break
            queue = list(localVisited)
            for word in queue:
                wordList.remove(word)
        
        self.ans = []
        printPath(endWord, [])
        return self.ans