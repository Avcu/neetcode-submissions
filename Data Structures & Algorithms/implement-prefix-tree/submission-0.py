class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        iteNode = self.root

        for i in range(len(word)):
            currCh = word[i]
            idx = ord(currCh) - ord('a')
            if iteNode.children[idx]:
                iteNode = iteNode.children[idx]
                if i == len(word) - 1:
                    iteNode.endWord = True
            else:
                newNode = TrieNode()
                if i == len(word) - 1:
                    newNode.endWord = True
                iteNode.children[idx] = newNode
                iteNode = iteNode.children[idx]

    def search(self, word: str) -> bool:
        iteNode = self.root

        for i in range(len(word)):
            currCh = word[i]
            idx = ord(currCh) - ord('a')

            if iteNode.children[idx] is None:
                return False
            iteNode = iteNode.children[idx]
        if iteNode.endWord:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        iteNode = self.root

        for i in range(len(prefix)):
            currCh = prefix[i]
            idx = ord(currCh) - ord('a')

            if iteNode.children[idx] is None:
                return False
            iteNode = iteNode.children[idx]
        return True
        