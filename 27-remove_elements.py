class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        num_removed = 0

        i = 0
        while (i < length - num_removed):
            if (nums[i+num_removed] == val):
                #Remove the value.
                num_removed += 1

            index = i + num_removed
            if (index < length):
                nums[i] = nums[index]
                if (nums[i] != val):
                    i+= 1

        return (length - num_removed)
    