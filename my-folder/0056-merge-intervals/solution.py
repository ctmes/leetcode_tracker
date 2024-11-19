class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Step 1: Sort intervals by their start times
        intervals.sort(key=lambda x: x[0])

        # Step 2: Initialize the output with the first interval
        output = [intervals[0]]

        # Step 3: Iterate through the intervals
        for i in range(1, len(intervals)):
            current = intervals[i]
            last_in_output = output[-1]

            # If the current interval overlaps with the last one in the output
            if current[0] <= last_in_output[1]:
                # Merge them by updating the end of the last interval in output
                last_in_output[1] = max(last_in_output[1], current[1])
            else:
                # Otherwise, add the current interval as a new one
                output.append(current)

        return output
        
