class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        ans, arr, smallest = [], sorted(arr), inf
        for num1, num2 in zip(arr[1:], arr[:-1]):
            smallest = min(smallest, abs(num1 - num2))
        for num1, num2 in zip(arr[:-1], arr[1:]):
            if abs(num1 - num2) == smallest: ans.append([num1, num2])
        return ans
        
        