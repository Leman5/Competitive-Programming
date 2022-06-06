class Solution:
    def reverse(self, x: int) -> int:
        sign_multiplier = 1
        if x < 0: 
            sign_multiplier = -1
            x = x * sign_multiplier

        rev = 0
        min_int_32 = 2 ** 31
        while x > 0:
            # Add the current digit into result
            rev= rev * 10 + x % 10
            
            # Check if the result is within MaxInt32 and MinInt32 bounds
            if rev * sign_multiplier <= -min_int_32 or rev * sign_multiplier >= min_int_32-1:
                return 0
            x = x // 10

        # Restore to original sign of number (+ or -)
        return sign_multiplier * rev
        