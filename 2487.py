# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head

        while current:
            stack.append(current.val)
            current = current.next


        max_val = float('-inf')
        rstack = []

        while stack:
            val = stack.pop()
            if val >= max_val:
                max_val = val
                rstack.append(val)

        dummy = head
        current = dummy

        for val in reversed(rstack):
            current.next =ListNode(val)
            current = current.next

        return dummy.next

        
