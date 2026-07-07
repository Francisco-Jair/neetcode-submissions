class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        min_valeu = min(nums)
        max_value = max(nums)

        bucket_count = max_value - min_valeu + 1
        buckets = [0] * bucket_count


        for num in nums:
            buckets[num - min_valeu] += 1
        
        # Create a list of (count, value) pairs for all elements that appeared
        frequencies = []
        for i, count in enumerate(buckets):
            if count > 0:
                value = i + min_valeu
                frequencies.append((count, value))
        
        # Sort pairs by frequency descending
        frequencies.sort(key=lambda x: x[0], reverse=True)

        # Return the values of the top k pairs
        return [pair[1] for pair in frequencies[:k]]