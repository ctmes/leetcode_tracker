# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]

        def height(root):
            if not root:
                return False

            LH = height(root.left)
            
            # if theres an issue, stop immediately
            if balanced[0] is False:
                return 0

            RH = height(root.right)

            if balanced[0] is False:
                return 0

            if abs(LH - RH) > 1:
                balanced[0] = False
                return False

            return 1 + max(LH, RH)

        height(root)
        return balanced[0]

    

