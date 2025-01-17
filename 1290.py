# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        decval = []
        while head:
            decval.append(head.val)
            head = head.next
        decval = ''.join(map(str , decval))
        binval = int(decval, 2)

        return binval

        
