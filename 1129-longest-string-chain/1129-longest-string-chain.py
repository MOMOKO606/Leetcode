class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words, visited, ans = sorted(words, key=len, reverse=True), set(), 1
        for word in words:
            if word in visited: continue
            deque = collections.deque([(word, 1)])
            while deque:
                node, count = deque.popleft()
                ans = max(ans, count)
                for i in range(len(node)):
                    predecessor = node[:i] + node[i + 1:]
                    if predecessor in words and predecessor not in visited:
                        deque.append((predecessor, count + 1))
                        visited.add(predecessor)
        return ans