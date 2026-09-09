class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.dummyNodeStart = Node(0, 0)
        self.dummyNodeEnd = Node(0, 0)
        self.dummyNodeStart.next = self.dummyNodeEnd
        self.dummyNodeEnd.prev = self.dummyNodeStart

        self.nodeMapping = {}
        self.capacity = capacity

    def _removeNode(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def _addNodeToEnd(self, key, value):
        prevNode = self.dummyNodeEnd.prev
        newNode = Node(key, value)
        newNode.prev = prevNode
        newNode.next = self.dummyNodeEnd

        prevNode.next = newNode
        self.dummyNodeEnd.prev = newNode
        return newNode
        

    def get(self, key: int) -> int:
        if key not in self.nodeMapping:
            return -1
        
        node = self.nodeMapping[key]
        self._removeNode(node)
        self.nodeMapping[key] = self._addNodeToEnd(key, node.val)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.nodeMapping:
            self._removeNode(self.nodeMapping[key])
        self.nodeMapping[key] = self._addNodeToEnd(key, value)
        
        if len(self.nodeMapping) > self.capacity:
            keyToRemove = self.dummyNodeStart.next.key
            self._removeNode(self.nodeMapping[keyToRemove])
            self.nodeMapping.pop(keyToRemove)


        
