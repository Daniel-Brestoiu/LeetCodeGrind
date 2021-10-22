class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer = int("".join(map(str, digits))) + 1
        digits = [char for char in str(integer)]
        return digits