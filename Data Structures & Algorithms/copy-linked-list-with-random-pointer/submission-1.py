"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        arr = []
        newArr = []
        lookUp = {}

        curr = head
        idx = 0
        while curr:
            newNode = Node(x=curr.val)

            arr.append(curr)
            newArr.append(newNode)

            lookUp[curr] = idx
            curr = curr.next
            idx += 1

        for idx in range(len(arr)):
            if idx > 0:
                newArr[idx-1].next = newArr[idx]
            if arr[idx].random:
                idxRandom = lookUp[arr[idx].random]
                newArr[idx].random = newArr[idxRandom]

        return newArr[0]

        

        