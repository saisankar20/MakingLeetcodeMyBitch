# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        stack1 = []
        

        while l1:
            stack.append(l1.val)
            l1 = l1.next

        while l2:
            stack1.append(l2.val)
            l2 = l2.next


        result = int("".join(map(str, stack))) + int("".join(map(str, stack1)))
        result = list(map(int, str(result)))
        result =result[::-1]

        head = ListNode(result[0])
        current = head

        for val in result[1:]:
            current.next = ListNode(val)
            current = current.next

        return head

#22/1569
        



        
