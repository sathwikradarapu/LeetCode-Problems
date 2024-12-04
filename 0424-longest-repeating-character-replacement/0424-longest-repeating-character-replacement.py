class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict

        l = 0
        n = len(s)
        freq = defaultdict(int)
        max_freq = 0  # Maximum frequency of any character in the current window
        ans = 0

        for r in range(n):
            freq[s[r]] += 1
            max_freq = max(max_freq, freq[s[r]])

            # If the number of changes required exceeds k, shrink the window
            while (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans


