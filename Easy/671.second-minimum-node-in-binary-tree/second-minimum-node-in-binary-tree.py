# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1


        treeSet = set()
        self.postOrder(root, treeSet)
        treeSet = sorted(treeSet)


        if len(treeSet) == 1:
            return -1
        else:
            return treeSet[1]

    def postOrder(self, root, treeSet):

        if not root:
            return

        self.postOrder(root.left, treeSet)
        self.postOrder(root.right, treeSet)

        treeSet.add(root.val)
