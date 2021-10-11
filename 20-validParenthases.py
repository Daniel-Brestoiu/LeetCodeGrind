class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairsDict = {"(": ")", "[": "]", "{":"}"}
        
        for i in range(0, len(s)):
            if (s[i] in pairsDict ):
                stack.append(s[i])
            elif (s[i] in pairsDict.values() ):
                if (not stack):
                    return False
        
                if (pairsDict[stack[-1]] == s[i]):
                    stack.pop(-1)
                else:
                    return False
        if (len(stack) == 0):
            return True
        else:
            return False