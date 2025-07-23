class Solution:
    def reverse(self, x: int) -> int:
        y = str(abs(x))[::-1]  # Reverse absolute value
        res = int(y)
        if x < 0:
            res = -res

        # Check 32-bit signed integer range
        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res
