class Solution:
    def alienOrder(self, words: List[str]) -> str:
        indegs, graph = {char: 0 for word in words for char in word}, collections.defaultdict(set)
        for word1, word2 in zip(words[:-1], words[1:]):
            for char1, char2 in zip(word1, word2):
                if char1 != char2:
                    if char2 not in graph[char1]:
                        graph[char1].add(char2)
                        indegs[char2] += 1
                    break
            else:
                if len(word1) > len(word2): return ""
        queue, ans = [node for node, value in indegs.items() if not value], ""
        count = len(queue)
        while queue:
            nextQueue = []
            for char in queue:
                ans += char
                for neigbhor in graph[char]:
                    indegs[neigbhor] -= 1
                    if not indegs[neigbhor]: 
                        nextQueue.append(neigbhor)
                        count += 1
            queue = nextQueue
        return ans if count == len(indegs) else ""
            
                
                    
                    

        