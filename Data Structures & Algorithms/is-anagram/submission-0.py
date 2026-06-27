class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        ht = {}

        for i in range(len(s)):
            if s[i] not in ht:
                ht[s[i]] = 1
            else:
                ht[s[i]] += 1

            if t[i] not in ht:
                ht[t[i]] = -1
            else:
                ht[t[i]] -= 1
        

        for key, value in ht.items():
            if value != 0:
                return False
            
        return True