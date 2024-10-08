class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def print_path(word=endWord, seq=[]):
            if word == beginWord:
                seq += [word]
                ans.append(seq[::-1])
                return
            if word not in paths: return
            for neighbor in paths[word]:
                print_path(neighbor, seq + [word])

        wordLisr = set(wordList)
        if endWord not in wordList: return []
        if beginWord in wordList: wordList.remove(beginWord)
        queue, paths = [beginWord], {}
        while queue:
            localVisited = set([])
            for word in queue:
                for i in range(len(word)):
                    for char in "abcdefghijklmnopqrstuvwxyz":
                        newWord = word[:i] + char + word[i + 1:]
                        if newWord in wordList:
                            localVisited.add(newWord)
                            paths[newWord] = paths.get(newWord, []) + [word]
            for word in localVisited: wordList.remove(word)
            queue = list(localVisited)

        ans = []
        print_path()
        return ans
                

        