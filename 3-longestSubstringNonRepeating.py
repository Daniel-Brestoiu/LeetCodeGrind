def lengthOfLongestSubstring(s):
    #Hdict to know if char in string, str to maintain order.
    hdict = {}
    str_lst = []

    max_size = 0
    size = 0
    for char in s:
        if (char in hdict and str_lst[0] != char):
            #In dict and first is not matching. 
            if (size > max_size):
                max_size = size
            
            #Clear up until char can be added correctly
            while (str_lst[0] != None and str_lst[0] != char):
                leading_char = str_lst[0]
                hdict.pop(leading_char)
                str_lst.pop(0)
                size -= 1

            #Add char (consider may be empty list)
            if (str_lst[0] == char):
                str_lst.pop(0)
                size -= 1
            
            hdict[char] = 1
            str_lst.append(char)
            size += 1
            
        elif (char in hdict):
            #In dict but not first char.
            str_lst.pop(0)
            str_lst.append(char)
        else:
            #New char to add.
            size += 1
            hdict[char] = 1
            str_lst.append(char)
        
    return max(size, max_size)

print(lengthOfLongestSubstring("abcabcbc"))