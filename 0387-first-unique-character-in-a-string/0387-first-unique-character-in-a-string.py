class Solution:
    def firstUniqChar(self, s: str) -> int: 
        copyS = s
        # print(copyS)
        n = len(s)
        i = 0
        while True:
            if s[0] not in s[1:]:
                return copyS.index(s[0])
            else:
                s = s.replace(s[i], '')
                # print(s)
                n = len(s)
                if n == 1:
                    # print(s[0])
                    return copyS.index(s[0])
                elif n == 0:
                    return -1
