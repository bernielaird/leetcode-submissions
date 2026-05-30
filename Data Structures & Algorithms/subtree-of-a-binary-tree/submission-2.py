# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val != subRoot.val:
                return False
            left, right = isSame(root.left,subRoot.left), isSame(root.right,subRoot.right)
            return left and right
        def dfs(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if not root:
                return False
            temp = False
            if root.val == subRoot.val:
                temp = isSame(root,subRoot)
            left = dfs(root.left, subRoot)
            right = dfs(root.right, subRoot)
            return left or right or temp
        return dfs(root, subRoot)
            