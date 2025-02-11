from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1 or not head:
            return head  # No need to reverse if k is 1 or the list is empty

        # Step 1: Compute the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Step 2: Use a dummy node for easier manipulation
        dummy = ListNode(0)
        dummy.next = head
        prev_group_tail = dummy
        current = head

        # Step 3: Reverse k nodes at a time
        while length >= k:
            prev = None
            next_node = None
            temp_head = current  # Save the starting node of the current k-group

            # Reverse k nodes
            for _ in range(k):
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            
            # Connect the reversed part
            prev_group_tail.next = prev  # prev is the new head of this k-group
            temp_head.next = current  # Connect to next part of the list
            prev_group_tail = temp_head  # Move to the new tail

            # Reduce the length by k since we processed a full group
            length -= k
        
        return dummy.next  # Return new head of the modified list
