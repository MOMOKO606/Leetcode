class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        def helper(node, cur_word):
            if len(seq) == 3: return 
            if "#" in node: 
                seq.append(cur_word)
            for key in sorted(node.keys()):
                if key == "#": continue
                helper(node[key], cur_word + key)

            
        
        
        # Build the trie
        trie = {}
        for product in products:
            node = trie
            for char in product:
                node[char] = node.get(char, {})
                node = node[char]
            node["#"] = "#"

        ans = []
        for i, char in enumerate(searchWord):
            node, seq = trie, []
            for j in range(i + 1):
                if searchWord[j] not in node: 
                    ans.append([])
                    break
                node = node[searchWord[j]]
            else:
                helper(node, searchWord[:i + 1])
                ans.append(seq[:])
        return ans


        