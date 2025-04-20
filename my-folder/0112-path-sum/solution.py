# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def is_sum(root, curr_sum):
            if not root:
                return False

            curr_sum += root.val
            
            if root.left == None and root.right == None:
                return curr_sum == targetSum

            return is_sum(root.left, curr_sum) or is_sum(root.right, curr_sum)

        return is_sum(root, 0)

