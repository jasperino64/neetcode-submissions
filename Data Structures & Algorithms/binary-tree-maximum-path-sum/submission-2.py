# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        
        def dfs(root):
            
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            
            # don't include negative branches
            leftMax = max(leftMax, 0) 
            rightMax = max(rightMax, 0)
            
            # with split
            self.res = max(self.res, root.val + leftMax + rightMax) # path from left to right through root
            
            # without split
            return root.val + max(leftMax,rightMax) # path of branch

        dfs(root)
        return self.res