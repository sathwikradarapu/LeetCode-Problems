class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        #optimal
        length=len(intervals)
        result=[]
        index=0
        while index<length and intervals[index][1]<newInterval[0]:
            result.append(intervals[index])
            index+=1
        while index<length and intervals[index][0]<=newInterval[1]:
            newInterval[0]=min(intervals[index][0],newInterval[0])
            newInterval[1]=max(intervals[index][1],newInterval[1])
            index+=1
        result.append(newInterval)
        while index<length:
            result.append(intervals[index])
            index+=1
        return result