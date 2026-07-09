# 14. Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for i in range(len(strs[0])):
            ch = strs[0][i]
            for tu in strs[1:]:
                if i >= len(tu) or ch != tu[i]:
                    return result
            result += ch 
        return result
