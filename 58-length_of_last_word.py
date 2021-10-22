class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split(" ")
        for word in arr[::-1]:
            length = len(word)
            if (length > 0):
                #not space character,
                return (length)