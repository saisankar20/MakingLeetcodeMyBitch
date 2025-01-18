# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy_head = ListNode(0)
        current = dummy_head

        # Traverse both lists
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum and carry
            total = val1 + val2 + carry
            carry = total // 10

            # Create a new node for the current digit
            current.next = ListNode(total % 10)
            current = current.next

            # Move to the next nodes
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next
