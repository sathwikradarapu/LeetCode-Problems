class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=len(word1)
        l2=len(word2)
        def getNewString(word1,word2):
            new_string=""
            for i in range(min(l1,l2)):
                new_string+=word1[i]+word2[i]
            return new_string
        if l1==l2:
            new_string=getNewString(word1,word2)
        elif l1>l2:
            new_l1=word1[:l2]
            new_string=getNewString(new_l1,word2)
            new_string+=word1[l2:]
        else:
            new_l2=word2[:l1]
            new_string=getNewString(word1,new_l2)
            new_string+=word2[l1:]
        return new_string