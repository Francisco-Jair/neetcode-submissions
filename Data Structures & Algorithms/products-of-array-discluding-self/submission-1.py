class Solution:

    def query(self, prod, zero, l, r) -> int:
        zeros = zero[r+1] - zero[l]
        if zeros > 0:
            return 0
        
        return prod[r + 1] // prod[l]

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod = [1] * (n + 1)
        zero = [0] * (n + 1)


        for i, x in enumerate(nums):
            zero[i + 1] = zero[i] + (1 if x == 0 else 0)
            prod[i + 1] = prod[i] * (1 if x == 0 else x)
        

        ans = []

        for i in range(n):
            prod_last = self.query(prod, zero, 0, i-1) #O(1)
            prod_before = self.query(prod, zero, i+1, n-1) #O(1)

            ans.append(prod_last*prod_before)
        

        return ans

