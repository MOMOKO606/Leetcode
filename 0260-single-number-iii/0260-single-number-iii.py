class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor, first, second = 0, 0, 0
        for num in nums:
            xor ^= num
        xor &= -xor
        for num in nums:
            if num & xor: first ^= num
            else: second ^= num
        return [first, second]



        