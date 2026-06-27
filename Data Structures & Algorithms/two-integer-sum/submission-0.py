class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}

        for key, value in enumerate(nums):
            
            if ht.get(value, -1) >= 0:
                return [ht[value], key]
            
            if not ht.get(target-value):
                ht[target-value] = key
            