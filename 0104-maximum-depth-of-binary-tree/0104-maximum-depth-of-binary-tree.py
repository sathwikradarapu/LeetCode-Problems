# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res=float("-inf")
        def fun(root,level):
            nonlocal res
            if not root:
                return 
            else:
                fun(root.left,level+1)
                res=max(res,level)
                fun(root.right,level+1)
        fun(root,1)
        return res