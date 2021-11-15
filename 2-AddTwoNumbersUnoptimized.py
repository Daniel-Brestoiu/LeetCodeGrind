# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getNum(node, depth):
            if (node.next == None):
                return (node.val * 10 ** depth)
            else:
                given = getNum(node.next, depth + 1)
                new = (node.val * 10 ** depth) + given
                return new
            
        val1 = getNum(l1, 0)
        val2 = getNum(l2, 0)
        revNewSumStr = str(val1 + val2)[::-1]
        
        root = ListNode()
        current = root
        length = len(revNewSumStr)
        for index in range(0, length):
            current.val = revNewSumStr[index]
            if (index != length - 1):
                current.next = ListNode()
                current = current.next
            else:
                current.next = None
        
        return root
            
            
            