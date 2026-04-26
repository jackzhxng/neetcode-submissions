# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = -1

    def _rec(self, root) -> int:
        if not root:
            return 0
        left = self._rec(root.left)
        right = self._rec(root.right)
        self.res = max(left + right, self.res)
        return 1 + max(left, right)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Time taken: 4 min

        The rec returns the height of the tree/subtree. For each node in
        the recursion you can take the height of the left and right subtrees
        to find a potential max diameter.
        """
        _ = self._rec(root)
        return self.res
        