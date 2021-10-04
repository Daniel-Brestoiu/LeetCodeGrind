class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        valueDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M":1000 }
        
        for index in range(0, len(s) - 1):
            if (valueDict[s[index]] < valueDict[s[index + 1]]):
                sum -= valueDict[s[index]]
            else:
                sum += valueDict[s[index]]
                
        sum += valueDict[s[len(s) - 1]]
        
        return sum