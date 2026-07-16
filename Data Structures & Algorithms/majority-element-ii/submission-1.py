class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        hash_table = {}


        for num in nums:
            hash_table[num] = hash_table.get(num, 0) + 1

            if hash_table[num] > len(nums) // 3 and num not in ans:
                ans.append(num)
        

        return ans