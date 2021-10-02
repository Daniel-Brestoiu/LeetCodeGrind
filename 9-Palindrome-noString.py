class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        
        temp_x = x
        inc = 0
        rev_x = 0
        while (temp_x > 0):
            digit = temp_x % 10
            temp_x = (temp_x - digit) / 10
            rev_x = rev_x * 10 + digit
            inc += 1
        return (rev_x == x)