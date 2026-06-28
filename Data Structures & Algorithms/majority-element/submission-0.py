class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        major_value = len(nums) // 2

        for element in nums:
            if hash_map.get(element, 0) + 1 >= (major_value):
                return element
            else:
                hash_map[element] = hash_map.get(element, 1) + 1