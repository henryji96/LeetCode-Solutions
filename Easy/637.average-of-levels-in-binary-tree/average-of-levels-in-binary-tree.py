# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#BFS 1
class Solution1(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        queue = []
        nextLayer = []
        nextLayer.append(root)

        ans = []

        while nextLayer:
            while nextLayer:
                queue.append(nextLayer.pop())

            curNodeNum = 0
            curLayerSum = 0
            while queue:
                node = queue.pop()

                if node.left:
                    nextLayer.append(node.left)
                if node.right:
                    nextLayer.append(node.right)

                curNodeNum += 1
                curLayerSum += node.val
            ans.append(curLayerSum / curNodeNum)

        return ans

#BFS 2
class Solution2(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        queue = []
        queue.append(root)
        curLayerSize = len(queue)
        tempSize = curLayerSize
        curLayerSum = 0
        ans = []

        while queue:

            node = queue.pop(0)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            tempSize -= 1
            curLayerSum += node.val

            if tempSize == 0:
                ans.append(float(curLayerSum)/curLayerSize)
                curLayerSize = len(queue)
                tempSize = curLayerSize
                curLayerSum = 0

        return ans
        
