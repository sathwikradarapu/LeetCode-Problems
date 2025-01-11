class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dici={
            "N":[0,1],
            "S":[0,-1],
            "E":[1,0],
            "W":[-1,0]
        }
        visit=set()
        x,y=0,0
        for i in path:
            visit.add((x,y))
            dx,dy=dici[i]
            x,y=x+dx,y+dy
            if (x,y) in visit:
                return True
        return False