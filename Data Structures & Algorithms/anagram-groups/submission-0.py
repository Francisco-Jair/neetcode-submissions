class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ht = {}

        # for word in strs: # O(N)
        #     aux = "".join(sorted(word)) # O(L log L)

        #     if aux not in ht:
        #         ht[aux] = [word]
        #     else:
        #         ht[aux].append(word)
        

        # ans = []

        # for key, value in ht.items(): # O(N)
        #     ans.append(value)
        

        # return ans


        # BEST SOLUTION

        ht = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for ch in word:
                count[ord(ch) - ord('a')] += 1
            
            key = tuple(count)
            ht[key].append(word)
        

        return list(ht.values())
