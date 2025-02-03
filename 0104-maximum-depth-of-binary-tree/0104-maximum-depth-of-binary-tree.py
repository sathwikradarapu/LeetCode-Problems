# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # Return 0 if the tree is empty
        
        ans = float("-inf")  # Initialize ans with negative infinity

        def dfs(root, level):
            nonlocal ans
            if not root:
                return
            else:
                ans = max(ans, level)  # Update the max depth
                dfs(root.left, level + 1)
                dfs(root.right, level + 1)
        
        dfs(root, 1)
        return ans
