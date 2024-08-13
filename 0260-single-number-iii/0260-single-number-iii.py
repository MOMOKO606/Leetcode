class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num

        target, first, second = xor & -xor, 0, 0
        for num in nums:
            if num & target: first ^= num
            else: second ^= num
        return [first, second]
        