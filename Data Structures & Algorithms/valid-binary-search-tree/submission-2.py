# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, rmin, rmax):
            if not root:
                return True
            left = dfs(root.left, rmin, root.val)
            right = dfs(root.right, root.val, rmax)
            if not (rmin < root.val < rmax):
                return False
            return (left and right)
        return dfs(root, float("-inf"), float("inf"))