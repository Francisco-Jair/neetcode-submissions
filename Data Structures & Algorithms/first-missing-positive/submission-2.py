class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        _set = set()
        tam = 0
        smallest_value = float("inf")
        min_value = 1

        for num in nums:
            _set.add(num)
            if num >= 0:
                tam += 1

        for _ in range(tam+1):
            print(min_value)
            if min_value not in _set:
                if min_value < smallest_value:
                    smallest_value = min_value
            
            min_value += 1
        
        
        print(smallest_value)

        return smallest_value