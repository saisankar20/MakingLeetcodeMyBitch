# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def traverse(node: Optional[TreeNode]):
            if not node:
                return
            traverse(node.left)     # Visit left subtree
            traverse(node.right)    # Visit right subtree
            result.append(node.val) # Process current node
        
        traverse(root)
        return result
      
