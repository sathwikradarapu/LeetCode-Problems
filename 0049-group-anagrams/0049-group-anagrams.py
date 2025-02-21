class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dici={}
        for i in strs:
            j="".join(sorted(i))
            if j in dici:
                dici[j].append(i)
            else:
                dici[j]=[i]
        return list(dici.values())