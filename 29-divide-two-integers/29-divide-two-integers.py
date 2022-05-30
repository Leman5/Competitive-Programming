class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
		# we work with positive numbers only and worry about the sign in the end
        if dividend > 0 and divisor > 0 or dividend < 0 and divisor < 0:
            positiveSign = True
        else:
            positiveSign = False
        dividend, divisor = abs(dividend), abs(divisor)
		
        divisorBitLength = divisor.bit_length()
        dividendBitLength = dividend.bit_length()
        
        quotient = 0
        for i in reversed(range(dividendBitLength - divisorBitLength + 1)):
            if dividend >> i >= divisor:
                dividend -= divisor << i
                quotient |= 1 << i
        
		# min handles corner case -2 ** 31 / -1 = 2 ** 31
        return min(2 ** 31 - 1, quotient) if positiveSign else -quotient
        