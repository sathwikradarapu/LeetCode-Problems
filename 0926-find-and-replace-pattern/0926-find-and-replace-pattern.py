class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        list=[]
        for i in words:
            hash_map1={}
            hash_map2={}
            ans=True
            for j in range(len(pattern)):
                k=pattern[j]
                l=i[j]
                if k not in hash_map1 and l not in hash_map2:
                    hash_map1[k]=l
                    hash_map2[l]=k
                if k in hash_map1 and hash_map1[k]!=l:
                    ans=False
                if l in hash_map2 and hash_map2[l]!=k:
                    ans=False
            if ans:
                list.append(i)
        return list
                        