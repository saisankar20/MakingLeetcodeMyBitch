from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def find_middle(head):
            slow, fast = head, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow  # Fix: Return the middle node
        
        def reverse_list(head):
            prev = None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev  # Fix: Return the new head of reversed list

        # Step 1: Find the middle of the list
        middle = find_middle(head)
        
        # Step 2: Reverse the second half of the list
        second_half = reverse_list(middle)
        
        # Step 3: Compute maximum twin sum
        max_sum = 0
        first_half = head
        
        while second_half:
            twin_sum = first_half.val + second_half.val
            max_sum = max(max_sum, twin_sum)
            
            # Move to the next nodes
            first_half = first_half.next
            second_half = second_half.next
        
        return max_sum

# Test case
'''head = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
sol = Solution()
print(sol.pairSum(head))  # Output: 6'''
