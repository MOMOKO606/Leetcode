class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products, ans = sorted(products), []
        for i, char in enumerate(searchWord):
            suggestion = []
            for product in products:
                if i < len(product) and char == product[i]:
                    suggestion.append(product)
            ans.append(suggestion[:3])
            products = suggestion
        return ans
        