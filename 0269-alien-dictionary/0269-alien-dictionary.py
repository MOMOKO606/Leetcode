class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Build the graph
        graph = collections.defaultdict(set)
        indegs = {char: 0 for word in words for char in word}
        for word1, word2 in zip(words[:-1], words[1:]):
            for char1, char2 in zip(word1, word2):
                if char1 != char2:
                    if char2 not in graph[char1]:
                        graph[char1].add(char2)
                        indegs[char2] = indegs.get(char2, 0) + 1
                    break
            else:
                if len(word1) > len(word2): return ''

        # BFS
        queue, ans = [char for char in indegs if not indegs[char]], ''
        while queue:
            nextQueue = []
            for char in queue:
                ans += char
                for neigbhor in graph[char]:
                    indegs[neigbhor] -= 1
                    if not indegs[neigbhor]: 
                        nextQueue.append(neigbhor)
            queue = nextQueue
        return ans if len(ans) == len(indegs) else ''

        