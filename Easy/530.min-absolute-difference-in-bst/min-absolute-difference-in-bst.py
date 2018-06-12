# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        orderedList = []
        self.inOrder(root, orderedList)

        minDiff = sys.maxsize
        for i in range(1, len(orderedList)):
            minDiff = min(minDiff, abs(orderedList[i] - orderedList[i-1]))
        return minDiff


    def inOrder(self, root, orderedList):

        if root == None:
            return
        self.inOrder(root.left, orderedList)
        orderedList.append(root.val)
        self.inOrder(root.right, orderedList)
