# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if (l1 == None and l2 == None):
            return
        
        l3 = ListNode()
        current_node = l3
        while (l1 != None and l2 != None):
            next_node = ListNode()

            if (l1.val > l2.val):
                current_node.val = l2.val
                l2 = l2.next
                current_node.next = next_node
                current_node = current_node.next
            elif (l1.val <= l2.val):
                current_node.val = l1.val
                l1 = l1.next
                current_node.next = next_node
                current_node = current_node.next
             
        if (l1 == None):
            current_node.val = l2.val
            current_node.next = l2.next
        elif (l2 == None):
            current_node.val = l1.val
            current_node.next = l1.next
        return (l3)
        