# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0  # base case
            
            count = 0
            if node.val >= max_so_far:
                count = 1  # Current node is good
            
            # Update max and recurse deeper
            new_max = max(max_so_far, node.val)
            
            # Count good nodes in left and right subtrees
            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)

            return count
        
        return dfs(root, root.val)
