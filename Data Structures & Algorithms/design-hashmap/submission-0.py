class MyHashMap:

    def __init__(self):
        self.capacity = 10**5
        self.arr = [[] for _ in range(self.capacity)]

    def put(self, key: int, value: int) -> None:
        idx = hash(key) % self.capacity
        for iteDict in self.arr[idx]:
            if key in iteDict:
                iteDict[key] = value
                return
        newDict = {key: value}
        self.arr[idx].append(newDict)

    def get(self, key: int) -> int:
        idx = hash(key) % self.capacity
        for iteDict in self.arr[idx]:
            if key in iteDict:
                return iteDict[key]
        return -1

    def remove(self, key: int) -> None:
        idx = hash(key) % self.capacity
        for iteDict in self.arr[idx]:
            if key in iteDict:
                self.arr[idx].remove(iteDict)
                return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)