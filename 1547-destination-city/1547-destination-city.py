class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        res=set()
        for i in paths:
            res.add(i[0])
        for i in paths:
            if i[1] not in res:
                return i[1]