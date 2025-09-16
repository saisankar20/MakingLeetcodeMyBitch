# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr  = []
        for head in lists:
        
            curr = head
            while curr:
                arr.append(curr.val)
                curr = curr.next
        
        if not arr:
            return None

        arr.sort()

        d = ListNode(0)
        t = d
        for v in arr:
            t.next = ListNode(v)
            t = t.next

            pass
        return d.next

        
