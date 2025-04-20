# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def prefix_sum_path(node, curr_sum, prefix_sums):
            if not node:
                return 0
            
            curr_sum += node.val
            count = prefix_sums.get(curr_sum - targetSum, 0)
            
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
            
            count += prefix_sum_path(node.left, curr_sum, prefix_sums)
            count += prefix_sum_path(node.right, curr_sum, prefix_sums)
            
            prefix_sums[curr_sum] -= 1
            if prefix_sums[curr_sum] == 0:
                del prefix_sums[curr_sum]
                
            return count
        
        return prefix_sum_path(root, 0, {0: 1})
