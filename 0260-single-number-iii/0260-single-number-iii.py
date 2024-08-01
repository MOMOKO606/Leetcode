class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor, first, second = 0, 0, 0
        for num in nums:
            xor ^= num
        
        target = 1
        while not xor & target:
            target <<= 1

        for num in nums:
            if num & target: first ^= num
            else: second ^= num
        return [first, second]



        