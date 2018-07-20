# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ans = []

        def inOrder(root):
            if not root:
                return

            inOrder(root.left)
            self.ans.append(root.val)
            inOrder(root.right)

        inOrder(root)

        return self.ans
