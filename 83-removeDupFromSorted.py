# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        numRemoved = 0
        # first = head
        lastGood  = head
        current = head
        while (current != None):
            if (lastGood.val == current.val):
                lastGood.next = current.next
            else:
                lastGood = current
            current = current.next
        
        return head