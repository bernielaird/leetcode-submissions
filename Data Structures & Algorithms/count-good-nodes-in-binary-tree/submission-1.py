# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, Max):
            if not root:
                return 0
            temp = max(Max, root.val)
            left = dfs(root.left, temp)
            right = dfs(root.right, temp)
            if root.val >= Max:
                return 1 + left + right
            else:
                return left + right
        return dfs(root, -101)