class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        def parent(i):
            root = i
            while p[root] != root:
                root = p[root]
            while p[i] != i:
                p[i], i = root, p[i]
            return root

        def connect(i, j):
            pi, pj = parent(i), parent(j)
            p[pi] = pj

        if len(sentence1) != len(sentence2): return False
        words = set()
        for word1, word2 in similarPairs:
            words.add(word1)
            words.add(word2)

        for word in sentence1 + sentence2:
            words.add(word)

        word_to_index = {word: i for i, word in enumerate(words)}
        p = [i for i in range(len(word_to_index))]

        for word1, word2 in similarPairs:
            i, j = word_to_index[word1], word_to_index[word2]
            connect(i, j)

        for word1, word2 in zip(sentence1, sentence2):
            pi, pj = parent(word_to_index[word1]), parent(word_to_index[word2])
            if pi != pj: return False
        return True
            

        
            
            

        