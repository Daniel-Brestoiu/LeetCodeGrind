# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def makeTree(nums):
            if (len(nums) == 0):
                return None
            middle_point = len(nums) // 2
            root = TreeNode(nums[middle_point])
            root.left = makeTree(nums[0:middle_point])
            root.right = makeTree(nums[middle_point+1:])
            return root
        
        return makeTree(nums)