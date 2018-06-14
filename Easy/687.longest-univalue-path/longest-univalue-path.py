# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self.ans = 0
        self.depth(root)
        return self.ans


    def depth(self, node):
        if not node:
            return 0

        leftDepth = self.depth(node.left)
        rightDepth = self.depth(node.right)

        left, right = 0, 0
        if node.left != None and node.left.val == node.val:
            left = leftDepth + 1
        if node.right != None and node.right.val == node.val:
            right = rightDepth + 1

        self.ans = max(self.ans, left + right)

        return max(left, right)
