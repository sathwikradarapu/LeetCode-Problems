class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map={}
        res=[]
        for i in strs:
            j=" ".join(sorted(i))
            if j in hash_map:
                hash_map[j].append(i)
            else:
                hash_map[j]=[i]
        return hash_map.values()