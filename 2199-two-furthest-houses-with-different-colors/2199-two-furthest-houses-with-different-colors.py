class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_distance=0
        for i in range(len(colors)):
            for j in range(1,len(colors)):
                if colors[i]!=colors[j]:
                    distance=abs(i-j)
                    max_distance=max(distance,max_distance)
        return max_distance