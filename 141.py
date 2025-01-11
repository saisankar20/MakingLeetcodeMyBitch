# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow, fast = head, head

        while fast and fast.next:  # Check both fast and fast.next
            slow = slow.next
            fast = fast.next.next

            if slow == fast:  # Cycle detected
                return True

        return False  # No cycle found
