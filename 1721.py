class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        stack = []
        position = 0

        # Collect all node values in a stack
        while current:
            stack.append(current.val)
            current = current.next
            position += 1

        # Correct the indices for 1-based k
        kth_index = k - 1
        opposite_index = position - k

        # Swap the values in the stack
        stack[kth_index], stack[opposite_index] = stack[opposite_index], stack[kth_index]

        # Update the linked list with swapped values
        current = head
        i = 0
        while current:
            current.val = stack[i]
            current = current.next
            i += 1

        return head
