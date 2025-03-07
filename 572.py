class Solution:
    
    # Helper function to check if two trees are exactly the same
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        # Check left and right subtree matches
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))
    
    # Main function to check if subRoot is a subtree of root
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        # First check if current nodes are identical, else check children
        return (self.isSameTree(root, subRoot) or 
                self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))
