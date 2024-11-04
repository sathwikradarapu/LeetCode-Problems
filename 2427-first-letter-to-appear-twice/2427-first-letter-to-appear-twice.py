class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hash_set=set()
        for i in s:
            if i not in hash_set:
                hash_set.add(i)
            else:
                return i