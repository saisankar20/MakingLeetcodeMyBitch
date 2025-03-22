# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = deque([root])
        if not root:
            return []

        while queue:
            ls = len(queue)
            cl = []

            for _ in range(ls):
                node = queue.popleft()
                cl.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
            result.append(cl)

        return result
    

        
