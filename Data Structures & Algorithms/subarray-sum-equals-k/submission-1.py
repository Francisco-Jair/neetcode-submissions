class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        freq = defaultdict(int)
        freq[0] = 1
        total = 0

        for num in nums:
            prefix_sum += num
            total += freq[prefix_sum-k]
            freq[prefix_sum] += 1
        

        return total
                