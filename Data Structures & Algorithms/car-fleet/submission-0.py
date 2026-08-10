class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posTimeList = []
        for idx in range(len(position)):
            posTimeList.append([position[idx], (target-position[idx])/speed[idx]])
        
        posTimeList.sort(key=lambda x: x[0])

        fleetCount = 0
        fleetStack = []
        for idx in range(len(posTimeList)-1,-1,-1):
            currTime = posTimeList[idx][1]
            if not fleetStack:
                fleetStack.append(currTime)
            else:
                if fleetStack[-1] < currTime:
                    fleetStack.append(currTime)

        return len(fleetStack)