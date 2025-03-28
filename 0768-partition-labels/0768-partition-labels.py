class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letters, intervals = set(s), []
        for letter in letters:
            intervals.append([s.find(letter), s.rfind(letter)])
        intervals.sort()
        cur_left, cur_right, ans = intervals[0][0], intervals[0][1], []
        for i in range(1, len(intervals)):
            if intervals[i][0] < cur_right:
                cur_right = max(cur_right, intervals[i][1])
            else:
                ans.append(cur_right - cur_left + 1)
                cur_left, cur_right = intervals[i][0], intervals[i][1]
        return ans + [cur_right - cur_left + 1]

            
        