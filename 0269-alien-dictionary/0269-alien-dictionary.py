class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Build the graph
        graph, indegs = collections.defaultdict(list), {char: 0 for word in words for char in word}
        for word1, word2 in zip(words[:-1], words[1:]):
            for char1, char2 in zip(word1, word2):
                if char1 != char2:
                    if char2 not in graph[char1]:
                        indegs[char2] += 1
                        graph[char1].append(char2)
                    break
            else:
                if len(word1) > len(word2): return ""

        queue, ans = [char for char in indegs.keys() if not indegs[char]], ""
        while queue:
            nextQueue = []
            for node in queue:
                ans += node
                for neighbor in graph[node]:
                    indegs[neighbor] -= 1
                    if not indegs[neighbor]:
                        nextQueue.append(neighbor)
            queue = nextQueue
        return ans if len([value for value in indegs.values() if not value]) == len(indegs) else ""


        