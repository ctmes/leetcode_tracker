# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        out = []
        
        def helper(root, curr_sum, nums_so_far):
            if not root:
                return
            
            # Update the current sum and path
            curr_sum += root.val
            nums_so_far.append(root.val)
            
            # Check if we are at a leaf node and the sum matches targetSum
            if not root.left and not root.right and curr_sum == targetSum:
                out.append(nums_so_far[:])  # Add a copy of the current path
            
            # Recurse on left and right children
            helper(root.left, curr_sum, nums_so_far)
            helper(root.right, curr_sum, nums_so_far)
            
            # Backtrack: remove the current node from the path
            nums_so_far.pop()
        
        helper(root, 0, [])
        return out
