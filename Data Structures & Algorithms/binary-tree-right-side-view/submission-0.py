# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root])

        while q:
            qlen = len(q)
            rightNode = None
            for _ in range(qlen):
                node = q.popleft()
                if node:
                    rightNode = node
                    node.left and q.append(node.left)
                    node.right and q.append(node.right)
            if rightNode:
                res.append(rightNode.val)
        
        return res
