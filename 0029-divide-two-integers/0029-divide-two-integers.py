class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Define INT_MAX and INT_MIN
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == divisor:
            return 1
        
        # Determine the sign of the result
        sign = True
        if (dividend >= 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = False
        
        # Work with absolute values
        n = abs(dividend)
        d = abs(divisor)
        ans = 0
        
        # Perform division using bit manipulation
        while n >= d:
            cnt = 0
            while n >= (d << (cnt + 1)):
                cnt += 1
            ans += (1 << cnt)
            n -= (d << cnt)
        
        # Apply sign and check for overflow
        if sign:
            if ans >= INT_MAX:
                return INT_MAX
            return ans
        else:
            if ans > INT_MAX:
                return INT_MIN
            return -ans
