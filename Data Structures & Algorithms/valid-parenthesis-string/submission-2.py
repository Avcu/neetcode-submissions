class Solution:
    def checkValidString(self, s: str) -> bool:
        l = []
        star = []
        for idx in range(len(s)):
            ch = s[idx]
            if ch == "(":
                l.append(idx)
            elif ch == "*":
                star.append(idx)
            else:
                if l:
                    l.pop()
                elif star:
                    star.pop()
                else:
                    return False

        while l and star:
            # make sure that stars are coming after the left parenthesis
            if star.pop() > l.pop():
                continue
            else:
                return False
        return not l