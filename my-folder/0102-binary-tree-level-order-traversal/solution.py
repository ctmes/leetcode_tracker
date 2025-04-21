# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        # if root

        q = deque()
        q.append(root)
        out = []

        while q:
            level = []
            n = len(q) # n is the length of the upcoming level
            
            for i in range(n):
                node = q.popleft()
                level.append(node.val)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            out.append(level)

        return out

