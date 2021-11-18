import math
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        
        i = 0
        j = 0
        newlist = []
        while i < len1 and j < len2:
            val1 = nums1[i]
            val2 = nums2[j]
            if (val1 < val2):
                newlist.append(val1)
                i += 1
            elif (val2 <= val1):
                newlist.append(val2)
                j += 1
            
        newlist = newlist + nums1[i:] + nums2[j:]
        #List is now sorted.
        
        total_len = len1 + len2
        if (total_len % 2 == 0):
            #Even. 
            decimal_middle = total_len // 2
            median = (newlist[decimal_middle - 1] + newlist[decimal_middle] ) /2
            return median
        
        else:
            #Odd
            middle = math.floor(total_len / 2)
            return newlist[middle]