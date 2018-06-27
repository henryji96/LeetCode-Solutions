class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)


    def pop(self):
        """
        :rtype: void
        """
        lenStack = len(self.stack)
        self.stack.pop(lenStack - 1)


    def top(self):
        """
        :rtype: int
        """
        lenStack = len(self.stack)
        return self.stack[lenStack - 1]


    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
