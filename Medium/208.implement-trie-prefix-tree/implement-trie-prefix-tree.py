class Trie(object):

    class Node(object):
        def __init__(self, val):
            self.val = val
            self.children = {}
            self.isWord = False



    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node(0)



    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """

        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = self.Node(c)
            cur = cur.children[c]
        cur.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return cur.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
