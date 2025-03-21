class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives, tens = 0, 0
        for bill in bills:
            if bill == 5: fives += 1
            if bill == 10: fives, tens = fives - 1, tens + 1
            if bill == 20:
                if tens: tens, fives = tens - 1, fives - 1
                else: fives -= 3
            if fives < 0: return False
        return True
        