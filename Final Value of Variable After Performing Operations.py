class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        inc=['X++','++X']
        dec=['X--','--X']
        X=0
        for i in operations:
            if i in inc:
                X+=1
            else:
                X-=1
        return X
        
