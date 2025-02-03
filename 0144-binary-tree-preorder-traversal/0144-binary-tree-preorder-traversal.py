# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def fun(root):
            if not root:
                return
            else:
                res.append(root.val)
                fun(root.left)
                fun(root.right)
        fun(root)
        return res