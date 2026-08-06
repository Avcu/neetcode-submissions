class Solution:
    def isHappy(self, n: int) -> bool:
        uniqueNumbers = set()

        def sumOfSquaresOfDigits(n: int) -> int:
            result = 0
            while n > 0:
                curr_digit = n % 10
                result += curr_digit*curr_digit
                n = n // 10
            return result

        while sumOfSquaresOfDigits(n) != 1:
            n = sumOfSquaresOfDigits(n)
            if n in uniqueNumbers:
                return False
            else:
                uniqueNumbers.add(n)
        return True


        