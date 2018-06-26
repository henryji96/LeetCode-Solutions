# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        queue = []
        queue.append(root)
        nextLayer = []
        depth = 1

        tempSize = len(queue)

        while queue:
            node = queue.pop(0)
            tempSize -= 1

            if node.left:
                nextLayer.append(node.left)
            if node.right:
                nextLayer.append(node.right)

            if not node.left and not node.right:
                return depth

            if tempSize == 0:
                queue += nextLayer
                tempSize = len(nextLayer)
                depth += 1
                nextLayer = []
