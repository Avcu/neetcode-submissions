class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        arr = [0, 0]

        for b in bills:
            if b == 5:
                arr[0] += 1
            elif b == 10:
                if arr[0] == 0:
                    return False
                else:
                    arr[1] += 1
                    arr[0] -= 1
            else:
                if arr[1] >= 1 and arr[0] >= 1:
                    arr[1] -= 1
                    arr[0] -= 1
                elif arr[0] >= 3:
                    arr[0] -= 3
                else:
                    return False
        return True