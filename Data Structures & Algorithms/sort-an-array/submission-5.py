class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quicksort(nums)
        # return nums
    
    def quicksort(self, arr):
        if len(arr) <= 1:
            return arr
        

        pivot = arr[len(arr) // 2]

        left = []
        middle = []
        right = []

        for num in arr:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                middle.append(num)
        
        return self.quicksort(left) + middle + self.quicksort(right)
