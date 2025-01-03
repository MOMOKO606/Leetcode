class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans, products = [], sorted(products)
        for i in range(1, len(searchWord) + 1):
            count, seq = 0, []
            for product in products:
                if count == 3: break
                if product[:i] == searchWord[:i]:
                    count, seq = count + 1, seq + [product]
            ans.append(seq)
        return ans




        