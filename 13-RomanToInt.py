class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        i = 0
        valueDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M":1000 }
        
        while (i < len(s)):
            char = s[i]
            
            if (i == len(s) - 1):
                sum += valueDict[s[i]]
            elif (char == "I"):
                if (s[i + 1] == "V"):
                    sum += valueDict[s[i + 1]] - valueDict[s[i]]
                    i += 1
                elif (s[i + 1] == "X"):
                    sum += valueDict[s[i + 1]] - valueDict[s[i]]
                    i += valueDict[s[i]]
                else:
                    sum += 1
            elif (char == "V"):
                sum += valueDict[s[i]]
            elif (char == "X"):
                if (s[i + 1] == "L"):
                    sum += valueDict[s[i + 1]] - valueDict[s[i]]
                    i += 1
                elif (s[i + 1] == "C"):
                    sum += valueDict[s[i + 1]] - valueDict[s[i]]
                    i += 1
                else:
                    sum += valueDict[s[i]]
            elif (char == "L"):
                sum += valueDict[s[i]]
            elif (char == "C"):
                if (s[i + 1] == "D"):
                    sum += valueDict[s[i + 1]] - valueDict[s[i]]
                    i += 1
                elif (s[i + 1] == "M"):
                    sum += valueDict[s[i + 1]] - valueDict[s[i]]
                    i += 1
                else:
                    sum += valueDict[s[i]]
            elif (char == "D"):
                sum += valueDict[s[i]]
            elif (char == "M"):
                sum += valueDict[s[i]]
            
            i += 1
        
        return sum
                
                