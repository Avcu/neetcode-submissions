class Node:
    def __init__(self, val):
        self.val = val
        self.prev, self.next = None, None

class MyCircularQueue:

    def __init__(self, k: int):
        dummyNode = Node(val=0)
        dummyNode.prev, dummyNode.next = dummyNode, dummyNode

        self.root = dummyNode
        self.size = 0
        self.k = k
        
    def enQueue(self, value: int) -> bool:
        if self.size == self.k:
            return False
        else:

            newNode = Node(val=value)
            prevNode = self.root.prev

            newNode.next = self.root
            newNode.prev = prevNode

            prevNode.next = newNode
            self.root.prev = newNode
            self.size += 1
            return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        self.root.next = self.root.next.next
        self.root.next.prev = self.root
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.root.next.val

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.root.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()