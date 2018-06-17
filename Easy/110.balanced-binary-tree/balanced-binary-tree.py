# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True

        self.balanced = True

        self.calcHeight(root)

        return self.balanced


    def calcHeight(self, root):

        if not root:
            return 0

        leftHeight = self.calcHeight(root.left)
        rightHeight = self.calcHeight(root.right)

        if abs(leftHeight - rightHeight) >= 2:
            self.balanced = False
            return -1

        return 1 + max(leftHeight, rightHeight)
