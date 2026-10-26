class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        index = 0
        length = len(intervals)
        result = []

        # Left part: intervals that don't overlap
        while index < length and intervals[index][1] < newInterval[0]:
            result.append(intervals[index])
            index += 1

        # Middle part: merge overlapping intervals
        while index < length and intervals[index][0] <= newInterval[1]:
            newInterval[0] = min(intervals[index][0], newInterval[0])
            newInterval[1] = max(intervals[index][1], newInterval[1])
            index += 1

        result.append(newInterval)

        # Right part: remaining intervals
        while index < length:
            result.append(intervals[index])
            index += 1

        return result