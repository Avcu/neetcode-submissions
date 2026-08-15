class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for i in range(len(word)):
            idx = ord(word[i]) - ord('a')
            if curr.children[idx]:
                if i == len(word) - 1:
                    curr.children[idx].endWord = True
            else:
                newNode = TrieNode()
                if i == len(word) - 1:
                    newNode.endWord = True
                curr.children[idx] = newNode
            curr = curr.children[idx]

    def search(self, word: str) -> bool:
        def searchDfs(trieNode, word):
            if len(word) == 1:
                if word[0] == '.':
                    for child in trieNode.children:
                        if child and child.endWord:
                            return True
                    return False
                else:
                    idx = ord(word[0]) - ord('a')
                    return trieNode.children[idx] is not None and trieNode.children[idx].endWord
            else:
                res = False
                firstCh = word[0]
                if firstCh == '.':
                    for child in trieNode.children:
                        if child:
                            res = res or searchDfs(child, word[1:])
                else:
                    idx = ord(firstCh) - ord('a')
                    if not trieNode.children[idx]:
                        return False
                    else:
                        res = res or searchDfs(trieNode.children[idx], word[1:])
                return res
        
        return searchDfs(self.root, word) 

