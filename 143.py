# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        sec_half = slow.next
        slow.next = None
        prev = None
        current = sec_half
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        sec_half = prev

        fir_half , sec_half = head, sec_half
        while sec_half:
            temp1 , temp2 = fir_half.next , sec_half.next
            fir_half.next = sec_half
            sec_half.next = temp1
            fir_half , sec_half = temp1 , temp2

        

