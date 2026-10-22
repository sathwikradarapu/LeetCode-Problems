class Solution:
    def kthSmallest(self, root, k):
        result = []

        def inorder(root):
            if root:
                inorder(root.left)
                result.append(root.val)
                inorder(root.right)

        inorder(root)
        return result[k - 1]