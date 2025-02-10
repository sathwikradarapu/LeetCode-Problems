class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
        }
        n=len(s)
        total=0
        for i in range(n):
            j=roman_values[s[i]]
            if i+1<n and j<roman_values[s[i+1]]:
                total-=j
            else:
                total+=j
        return total

