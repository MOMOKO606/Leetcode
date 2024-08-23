class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr, min_diff, ans = sorted(arr), inf, []
        for j in range(1, len(arr)):
            diff = arr[j] - arr[j - 1]
            if diff < min_diff:
                min_diff, ans = diff, [[arr[j - 1], arr[j]]]
            elif diff == min_diff: ans.append([arr[j - 1], arr[j]])
        return ans

        