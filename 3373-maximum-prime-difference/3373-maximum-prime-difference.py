class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        is_prime = [True] * (max(nums) + 1)
        is_prime[1] = False
        for i in range(2, len(is_prime)):
            if not is_prime[i]: continue
            for j in range(2 * i, len(is_prime), i):
                is_prime[j] = False

        i, j = 0, len(nums) - 1
        while i <= j:
            if not is_prime[nums[i]]:
                i += 1
            elif not is_prime[nums[j]]: 
                j -= 1
            else: return j - i


        

        