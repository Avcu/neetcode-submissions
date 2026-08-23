class MyHashSet:

    def __init__(self):
        self.capacity = 10**5
        self.arr = [[] for _ in range(self.capacity)]

    def add(self, key: int) -> None:
        idx = hash(key) % self.capacity
        for elem in self.arr[idx]:
            if elem == key:
                return
        self.arr[idx].append(key)

    def remove(self, key: int) -> None:
        idx = hash(key) % self.capacity
        for iteIdx in range(len(self.arr[idx])):
            if self.arr[idx][iteIdx] == key:
                self.arr[idx].pop(iteIdx)
                return

    def contains(self, key: int) -> bool:
        idx = hash(key) % self.capacity
        for elem in self.arr[idx]:
            if elem == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)