# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _rec(self, root: Optional[TreeNode], l_max: int, r_min: int) -> bool:
        if not root:
            return True
        if not l_max < root.val < r_min:
            return False
        left = self._rec(root.left, l_max, root.val) # Bounded on the left by l_max from wherever the parent came from, bounded on the right by the parent itself.
        right = self._rec(root.right, root.val, r_min) # Bounded on the left by the parent iself, bounded on the right by r_min from wherever the parent came from.
        return left and right

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Time taken: 9 min
        """
        return self._rec(root, -float("inf"), float("inf"))
        