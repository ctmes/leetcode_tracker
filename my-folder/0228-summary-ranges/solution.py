class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:  # Handle the empty list
            return []
        
        ranges = []
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                # End of a range
                if start == nums[i - 1]:
                    ranges.append(f"{start}")
                else:
                    ranges.append(f"{start}->{nums[i - 1]}")
                start = nums[i]  # Start a new range
        
        # Add the final range
        if start == nums[-1]:
            ranges.append(f"{start}")
        else:
            ranges.append(f"{start}->{nums[-1]}")
        
        return ranges
