from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if node is None:
                return 0  # Height of an empty tree is 0

            left_height = height(node.left)
            right_height = height(node.right)

            # If any subtree is unbalanced, propagate -1 up the tree
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            
            return 1 + max(left_height, right_height)

        return height(root) != -1

    def balance_factor(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        
        def height(n):
            if n is None:
                return 0
            return 1 + max(height(n.left), height(n.right))

        left_height = height(node.left)
        right_height = height(node.right)

        return left_height - right_height

