import collections

class TrieNode():

    def __init__(self):

        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root

        for w in word:
            node = node.children[w]
        node.is_word = True


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def dfs(word,node):
            if not word:
                return node.is_word

            if word[0] in node.children:
                return dfs(word[1:],node.children[word[0]])
            elif word[0]=='.':
                return any(dfs(word[1:],node.children[i]) for i in node.children)

            else:
                return False

        return dfs(word,self.root)


#####################################################################
class WordDictionary(object):

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

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                newNode = self.Node(c)
                cur.children[c] = newNode
            cur = cur.children[c]
        cur.isWord = True


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.dfs(word, self.root)


    def dfs(self, word, node):

        if not word:
            return node.isWord

        if word[0] in node.children:
            return self.dfs(word[1:], node.children[word[0]])
        elif word[0] == '.':
            #for c in node.children:
            #    return self.dfs(word[1:], node.children[c])
            return any(self.dfs(word[1:],node.children[i]) for i in node.children)
        else:
            return False





# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
