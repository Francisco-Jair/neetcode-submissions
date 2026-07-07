class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = defaultdict(int)
        # freq = [[] for i in range(len(nums) + 1)]

        # for num in nums:
        #     count[num] += 1
        
        # for key, value in count.items():
        #     freq[value].append(key)


        # ans = []
        # for i in range(len(freq)-1, 0, -1):
        #     for n in freq[i]:
        #         ans.append(n)

        #         if len(ans) == k:
        #             return ans

        # other solution

        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        heap = [(-value, -key) for key, value in count.items()]
        heapq.heapify(heap)

        ans = []
        while k > 0 and heap:
            value, key = heapq.heappop(heap)
            ans.append(-key)
            k -= 1
        

        return ans