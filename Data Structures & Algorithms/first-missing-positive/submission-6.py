class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # _set = set()
        # tam = 0
        # smallest_value = float("inf")
        # min_value = 1

        # for num in nums:
        #     _set.add(num)
        #     if num >= 0:
        #         tam += 1

        # for _ in range(tam+1):
        #     if min_value not in _set:
        #         if min_value < smallest_value:
        #             smallest_value = min_value
            
        #     min_value += 1
        

        # return smallest_value

        values = set(nums)

        for value in range(1, len(nums) + 2):
            if value not in values:
                return value

        return -1