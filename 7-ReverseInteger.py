class Solution:
    def reverse(self, x: int) -> int:
        sizeMin = -2**31
        sizeMax = 2**31 - 1
        
        stringX = str(x)
        if stringX[0] == '-': 
            stringX = "-"+str(x*-1)[::-1]
        else:
            stringX = stringX[::-1]
        
        revX = int(stringX)    
        if (revX < sizeMin or revX > sizeMax):
            return 0
        else:
            return revX