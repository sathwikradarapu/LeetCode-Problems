class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) == 0 or len(t) == 0 or len(s) < len(t):
            return ""

        # Count frequency of characters in t
        t_hashmap = {}
        for char in t:
            t_hashmap[char] = t_hashmap.get(char, 0) + 1

        required = len(t_hashmap)  # Number of unique characters in t to match in s
        formed = 0  # Number of characters with matching frequency in the current window
        l, r = 0, 0  # Pointers for sliding window
        ans = float("inf"), 0, 0  # Length of window, start, end

        # Hash map to store characters in the current window
        window_counts = {}

        while r < len(s):
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in t_hashmap and window_counts[char] == t_hashmap[char]:
                formed += 1

            # Try and contract the window until it ceases to be 'desirable'
            while l <= r and formed == required:
                char = s[l]

                # Update the answer if this window is smaller
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by `l` is no longer a part of the window
                window_counts[char] -= 1
                if char in t_hashmap and window_counts[char] < t_hashmap[char]:
                    formed -= 1

                l += 1  # Move left pointer

            r += 1  # Keep expanding the window

        # Return the smallest window or an empty string if no such window exists
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]
