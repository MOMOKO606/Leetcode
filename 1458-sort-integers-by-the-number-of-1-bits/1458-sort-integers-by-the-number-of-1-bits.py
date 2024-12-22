class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def get_ones(num):
            count, ori = 0, num
            while num:
                num = num & (num - 1)
                count += 1
            return count, ori

        arr = sorted(arr)
        return sorted(arr, key=get_ones)
        