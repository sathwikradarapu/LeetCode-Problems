from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Initialize dictionaries with 0 for all people
        dici1 = {i: 0 for i in range(1, n + 1)}  # Outgoing trust (who trusts others)
        dici2 = {i: 0 for i in range(1, n + 1)}  # Incoming trust (who is trusted)

        # Populate the dictionaries
        for i, j in trust:
            dici1[i] += 1  # Person i trusts someone
            dici2[j] += 1  # Person j is trusted by someone

        # Check for the town judge
        for i in range(1, n + 1):
            if dici1[i] == 0 and dici2[i] == n - 1:
                return i

        return -1
