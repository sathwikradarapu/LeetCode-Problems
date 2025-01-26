class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        c=0
        def isPrefixAndSuffix(str1,str2):
            if str2.startswith(str1) and str2.endswith(str1):
                return True
            else:
                return False
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                res=isPrefixAndSuffix(words[i],words[j])
                if res==True:
                    c+=1
        return c