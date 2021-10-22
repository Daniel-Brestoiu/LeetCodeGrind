

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = -1
        carry = False
        if (digits[index] == 9):
            carry = True
        else:
            digits[index] += 1
            
        while (carry):
            digits[index] = 0
    
            if (digits[index] is digits[0]):
                #Case to add, if 99, then make 100.
                digits.insert(0, 1)
                break
            
            if (digits[index - 1] == 9):
                index -= 1
            else:
                digits[index - 1] += 1
                carry = False
            
        return digits    
            
        