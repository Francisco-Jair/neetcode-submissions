class Solution:
    def validPalindrome(self, s: str) -> bool:
        start, last = 0, len(s) - 1


        while start < last:
            if s[start] != s[last]:
                return self.isPalindrome(s, start + 1, last) or self.isPalindrome(s, start, last - 1)
            start += 1
            last -= 1


        return True
    

    def isPalindrome(self, s, start, last) -> bool:

        while start < last:
            if s[start] != s[last]:
                return False
            
            start += 1
            last -= 1
        

        return True