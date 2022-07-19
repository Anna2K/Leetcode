# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

class Solution:
    
        def isBalanced(self, root: Optional[TreeNode]) -> bool:
            if not root:
                return True

            return abs(maxDepth(root.left) - maxDepth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)