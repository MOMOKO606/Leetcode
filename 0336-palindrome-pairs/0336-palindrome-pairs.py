class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        headsTails, ans = {word: i for i, word in enumerate(words)}, []
        for i, word in enumerate(words):
            # Cut the word
            for j in range(len(word) + 1):
                left, right = word[:j], word[j:]
                # Check head + word
                if left == left[::-1] and right[::-1] in headsTails and headsTails[right[::-1]] != i: 
                    ans.append([headsTails[right[::-1]], i])
                # Check word + tail
                if right == right[::-1] and left[::-1] in headsTails and headsTails[left[::-1]] != i and len(word) != len(left): 
                    ans.append([i, headsTails[left[::-1]]])
        return ans


        
        