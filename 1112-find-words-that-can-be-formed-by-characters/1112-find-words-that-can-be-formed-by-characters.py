class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hashmap_1={}
        res=0
        for i in chars:
            if i not in hashmap_1:
                hashmap_1[i]=1
            else:
                hashmap_1[i]+=1
        for i in words:
            hashmap_2={}
            for j in i:
                if j not in hashmap_2:
                    hashmap_2[j]=1
                else:
                    hashmap_2[j]+=1
            ans=True
            for j in hashmap_2:
                if j not in hashmap_1 or hashmap_2[j]>hashmap_1[j]:
                    ans=False
                    break
            if ans:
                res+=len(i)
        return res