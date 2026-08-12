class TimeMap:

    def __init__(self):
        self.myDict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.myDict[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.myDict:
            return ""
        else:
            arr = self.myDict[key]
            if not arr or timestamp < arr[0][0]:
                return ""
            if timestamp >= arr[-1][0]:
                return arr[-1][1]

            l, r = 0, len(arr) - 1
            while l <= r:
                mid = (l+r) // 2
                midTimestamp = arr[mid][0]

                if midTimestamp == timestamp or mid == r or (midTimestamp < timestamp and arr[mid+1][0] > timestamp):
                    break
                else:
                    if midTimestamp > timestamp:
                        r = mid - 1
                    else:
                        l = mid + 1
            
            return arr[mid][1]
