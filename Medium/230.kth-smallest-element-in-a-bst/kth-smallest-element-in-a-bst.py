# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.val = []

        def inOrder(root):
            if not root:
                return None

            inOrder(root.left)
            self.val.append(root.val)
            inOrder(root.right)

        inOrder(root)

        return self.val[k-1]
