class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        aux = 0

        for value in nums:
            
            if value != 1:
                maxOnes = max(maxOnes, aux)
                aux = 0
                continue

            aux += 1
        

        return max(maxOnes, aux)