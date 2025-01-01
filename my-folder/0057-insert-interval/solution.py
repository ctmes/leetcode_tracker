from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval[0], newInterval[1]
        l = 0
        r = len(intervals) - 1
        
        while l <= r:
            m = (l + r) // 2
            
            # Check for overlap and merge logic
            if intervals[m][0] <= end and intervals[m][1] >= start:  # Overlapping intervals
                start = min(start, intervals[m][0])
                end = max(end, intervals[m][1])
                del intervals[m]  # Remove the merged interval
                r -= 1  # Adjust the upper bound after deletion
            elif intervals[m][1] < start:  # Current interval is entirely before newInterval
                l = m + 1
            else:  # Current interval is entirely after newInterval
                r = m - 1

        # Insert the merged interval
        intervals.insert(l, [start, end])
        
        return intervals

