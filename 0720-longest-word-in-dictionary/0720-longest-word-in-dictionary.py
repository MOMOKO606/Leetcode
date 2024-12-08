class Solution:
    def longestWord(self, words: List[str]) -> str:
        queue, wordSet, words, ans = [""], set(words), sorted(words), ""
        while queue:
            next_queue = []
            for word in queue:
                for char in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word + char
                    if new_word in wordSet:
                        wordSet.remove(new_word)
                        next_queue.append(new_word)
                        ans = max(ans, new_word, key=len)
            queue = next_queue
        return ans

        
        