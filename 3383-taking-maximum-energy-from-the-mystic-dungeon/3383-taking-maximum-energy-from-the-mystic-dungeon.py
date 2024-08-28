class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        energy = energy[::-1]
        ans = max(energy[:k])
        for i in range(k, len(energy)):
            energy[i] += energy[i - k]
            ans = max(ans, energy[i])
        return ans
        
        