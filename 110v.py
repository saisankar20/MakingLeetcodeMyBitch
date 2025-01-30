class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            
            left_height = height(node.left)
            if left_height == -1:
                return -1  # Left subtree is not balanced
            
            right_height = height(node.right)
            if right_height == -1:
                return -1  # Right subtree is not balanced
            
            if abs(left_height - right_height) > 1:
                return -1  # Current node is not balanced
            
            return max(left_height, right_height) + 1  # Return the height of the subtree
        
        return height(root) != -1
