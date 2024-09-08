class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_len=0
        for i in sentences:
            j=i.split()
            k=len(j)
            if max_len<k:
                max_len=k
        return max_len