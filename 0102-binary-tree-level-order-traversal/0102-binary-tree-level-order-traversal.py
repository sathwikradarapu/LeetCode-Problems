class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        else:
            queue=collections.deque([root])
            result=[]
            while queue:
                current_result=[]
                for _ in range(len(queue)):
                    node=queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    current_result.append(node.val)
                result.append(current_result)
            return result