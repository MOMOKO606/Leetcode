class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        target, smallest, ans = set(list1).intersection(set(list2)), inf, []
        list1 = {word: i for i, word in enumerate(list1)}
        list2 = {word: i for i, word in enumerate(list2)}
        for word in target:
            cur = list1[word] + list2[word]
            if cur < smallest:
                smallest, ans = cur, [word]
            elif cur == smallest:
                ans += [word]
        return ans

        