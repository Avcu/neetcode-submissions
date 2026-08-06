class Solution:
    def isValid(self, s: str) -> bool:
        myList = []

        for ch in s:
            if ch in ['(', '{', '[']:
                myList.append(ch)
            else:
                if len(myList) == 0:
                    return False
                    
                popped = myList.pop()
                if popped == '(' and ch == ')':
                    continue
                elif popped == '{' and ch == '}':
                    continue
                elif popped == '[' and ch == ']':
                    continue
                else:
                    return False
        return len(myList) == 0
                