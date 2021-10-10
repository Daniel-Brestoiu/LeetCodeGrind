class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        smallestWord = min(strs, key=len)
        longestPrefix = ""
        
        for i in range(0, len(smallestWord)):
            if (strs[0][i] == strs[-1][i]):
                longestPrefix = longestPrefix + strs[0][i]
            else:
                break
        
        return longestPrefix