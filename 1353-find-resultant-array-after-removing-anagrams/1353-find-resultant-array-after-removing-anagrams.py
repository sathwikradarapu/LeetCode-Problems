class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        hash_map={}
        res=[]
        for i in range(len(words)):
            if i==0:
                a=" ".join(sorted(words[i]))
                hash_map[a]=[words[i]]
                for i in hash_map.values():
                    res.extend(i)
                hash_map={}
            else:
                a=" ".join(sorted(words[i]))
                b=" ".join(sorted(words[i-1]))
                if a!=b:
                    if a in hash_map:
                        hash_map[a].append(words[i])
                        for i in hash_map.values():
                            res.extend(i)
                        hash_map={}
                    else:
                        hash_map[a]=[words[i]]
                        for i in hash_map.values():
                            res.extend(i)
                        hash_map={}
        return res
        