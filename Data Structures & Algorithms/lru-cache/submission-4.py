class LRUCache:

    def __init__(self, capacity: int):
        self.myDict = {}
        self.lruArr = []
        self.cap = capacity
        self.currSize = 0

    #  2, 3, 4, 1, 
    def get(self, key: int) -> int:
        if key in self.myDict:
            self.lruArr.remove(key)
            self.lruArr.append(key)
            return self.myDict[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.myDict and self.currSize == self.cap:
            # we need to remove the least recently used which is at idx 0
            poppedKey = self.lruArr.pop(0)
            self.myDict.pop(poppedKey)
        elif key not in self.myDict:
            self.currSize += 1

        if key in self.myDict:
                self.lruArr.remove(key)

        self.myDict[key] = value
        self.lruArr.append(key)