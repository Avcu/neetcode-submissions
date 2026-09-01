from collections import deque

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        numCountDict = defaultdict(int)
        distinct = set()
        
        for h in hand:
            numCountDict[h] = numCountDict.get(h, 0) + 1
            if h not in distinct:
                distinct.add(h)

        distinctList = list(distinct)
        distinctList.sort()
        q = deque(distinctList)
        while q:
            curVal = q.popleft()
            curValCount = numCountDict[curVal]

            if curValCount == 0:
                continue

            for i in range(groupSize):
                numCountDict[curVal+i] -= curValCount
                if numCountDict[curVal+i] < 0:
                    return False
        return True

