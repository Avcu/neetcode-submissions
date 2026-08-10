class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        myStack = []

        for idx in range(len(tokens)):
            currToken = tokens[idx]

            if currToken == "+" or currToken == "-" or currToken == "*" or currToken == "/":
                val2 = myStack.pop()
                val1 = myStack.pop()
                result = 0
                if currToken == "+":
                    result = val1 + val2
                if currToken == "-":
                    result = val1 - val2
                if currToken == "*":
                    result = val1 * val2
                if currToken == "/":
                    result = int(val1 / val2)
                myStack.append(result)
            else:
                myStack.append(int(currToken))
        return myStack[-1]