class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            # Check if the current digit is odd
            if int(num[i]) % 2 != 0:
                # Return the substring from the start to this odd digit
                return num[:i + 1]
        # If no odd number is found, return an empty string
        return ""