class CountSquares:

    def __init__(self):
       self.pointDict = defaultdict(int) 

    def add(self, point: List[int]) -> None:
        self.pointDict[tuple(point)] = self.pointDict.get(tuple(point), 0) + 1

    def count(self, point: List[int]) -> int:
        def findSquaresGivenTwoPoints(pointA, pointB):
            # x axis is the same for the given points
            aX, aY = pointA[0], pointA[1]
            bX, bY = pointB[0], pointB[1]
            sideLen = aY - bY
            if (aX+sideLen, aY) in self.pointDict and (aX+sideLen, bY) in self.pointDict:
                countB = self.pointDict[pointB]
                countReverseA = self.pointDict[(aX+sideLen, aY)]
                countReverseB = self.pointDict[(aX+sideLen, bY)]
                return countB * countReverseA * countReverseB
            if (aX-sideLen, aY) in self.pointDict and (aX-sideLen, bY) in self.pointDict:
                countB = self.pointDict[pointB]
                countReverseA = self.pointDict[(aX-sideLen, aY)]
                countReverseB = self.pointDict[(aX-sideLen, bY)]
                return countB * countReverseA * countReverseB
            return 0

        listX = []
        for k, v in self.pointDict.items():
            if point[0] == k[0] and point[1] != k[1]:
                listX.append(k)
        
        resInt = 0
        for x in listX:
            resInt += findSquaresGivenTwoPoints(point, x)
        return resInt
            

