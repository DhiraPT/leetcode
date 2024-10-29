class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        prefix = ''

        for c in searchWord:
            suggested = []
            prefix += c
            index = bisect.bisect_left(products, prefix)
            for i in range(index, min(index + 3, len(products))):
                if products[i].startswith(prefix):
                    suggested.append(products[i])
                else:
                    break
            res.append(suggested)

        return res