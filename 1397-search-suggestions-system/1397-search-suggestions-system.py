class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans, products = [], sorted(products)
        for i in range(len(searchWord)):
            next_products = []
            for product in products:
                if i < len(product) and searchWord[i] == product[i]:
                    next_products.append(product)
            ans.append(next_products[:3])
            products = next_products
        return ans
                
            

        