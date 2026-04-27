# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def _findPath(self, root: "TreeNode", target: int) -> list["TreeNode"]:
        if root.val == target:
            return [root]
        if root.val < target:
            path = self._findPath(root.right, target)
        else:
            path = self._findPath(root.left, target)
        return [root] + path

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Time taken: 13 mins

        Note - did not find the most optimal way to do it, although both are O(n). Most
        optimal way to do it involves utilizing the BST property better:
        https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solutions/6750689/video-all-you-have-to-do-is-just-to-unde-xl0q/
        """
        p_path = self._findPath(root, p.val)
        q_path = self._findPath(root, q.val)
        i = 0
        while i < len(p_path) and i < len(q_path) and p_path[i].val == q_path[i].val:
            i += 1
        return p_path[i - 1]