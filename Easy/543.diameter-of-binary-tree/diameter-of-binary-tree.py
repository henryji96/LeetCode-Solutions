# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:


    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def calcDepth(node):
            if not node:
                return 0
            leftDepth = calcDepth(node.left)
            rightDepth = calcDepth(node.right)

            self.ans = max(self.ans, leftDepth + rightDepth)
            return 1 + max(leftDepth, rightDepth)

        calcDepth(root)
        return self.ans

    def diameterOfBinaryTree2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def calcDepth(node):
            if not node:
                return 0
            leftDepth = calcDepth(node.left)
            rightDepth = calcDepth(node.right)

            if node.left != None:
                leftDepth = leftDepth + 1
            if node.right != None:
                rightDepth = rightDepth + 1
            self.ans = max(self.ans, leftDepth + rightDepth)
            return max(leftDepth, rightDepth)

        calcDepth(root)
        return self.ans
