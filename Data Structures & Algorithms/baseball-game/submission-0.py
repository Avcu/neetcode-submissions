class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        stack.append(int(operations[0]))

        for idx in range(1, len(operations)):
            currOp = operations[idx]

            if currOp == "+":
                stack.append(stack[-1]+stack[-2])
            elif currOp == "D":
                stack.append(2*stack[-1])
            elif currOp == "C":
                stack.pop()
            else:
                stack.append(int(currOp))
        return sum(stack)