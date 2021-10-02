class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0 ):
            return False
        
        x = str(x)
        length = len(x)
        i = 0
        while (x[i] == x[length - 1 - i]):
            if (length - 1 <= i):
                return(True)
            i += 1
        return False
