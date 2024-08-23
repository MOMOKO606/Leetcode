class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(n):
            j = i + 1
            if not j % 3 and not j % 5: ans.append("FizzBuzz")
            elif not j % 3: ans.append("Fizz")
            elif not j % 5: ans.append("Buzz")
            else: ans.append(str(j))
        return ans
        
        