# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = []
        queue.append(root)
        curSize = len(queue)

        ans = []
        ans.append([root.val])
        nextLayer = []
        nextLayerVal = []

        while queue:
            node = queue.pop(0)
            curSize -= 1

            if node.left:
                nextLayer.append(node.left)
                nextLayerVal.append(node.left.val)
            if node.right:
                nextLayer.append(node.right)
                nextLayerVal.append(node.right.val)

            if curSize == 0:
                curSize = len(nextLayer)
                queue += nextLayer
                if nextLayerVal != []:
                    ans.append(nextLayerVal)

                nextLayer = []
                nextLayerVal = []


        return ans[::-1]
