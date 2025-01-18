class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split the version strings into lists of integers
        version1 = list(map(int, version1.split(".")))
        version2 = list(map(int, version2.split(".")))

        # Find the maximum length of the two lists
        max_len = max(len(version1), len(version2))

        # Extend the shorter list with zeros
        version1.extend([0] * (max_len - len(version1)))
        version2.extend([0] * (max_len - len(version2)))

        # Compare each revision
        for i in range(max_len):
            if version1[i] < version2[i]:
                return -1
            elif version1[i] > version2[i]:
                return 1

        # If all revisions are equal
        return 0
