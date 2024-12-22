class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products, ans = sorted(products), []
        for i, char in enumerate(searchWord):
            suggestions = []
            for product in products:
                if i < len(product) and product[i] == char:
                    suggestions.append(product)
            suggestions = sorted(suggestions)
            ans.append(suggestions[:3])
            products = suggestions
        return ans

        