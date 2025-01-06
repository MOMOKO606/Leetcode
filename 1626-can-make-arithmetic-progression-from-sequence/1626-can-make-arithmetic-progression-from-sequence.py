class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr, deltas = sorted(arr), set()
        for num1, num2 in zip(arr[:-1], arr[1:]):
            deltas.add(num2 - num1)
        return len(deltas) == 1

        