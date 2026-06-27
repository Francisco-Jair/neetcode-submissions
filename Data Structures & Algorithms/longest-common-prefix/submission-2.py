class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        _min = min(strs)

        for i in range(len(_min)):
            for word in strs:
                if _min[i] != word[i]:
                    return _min[:i]

        return _min