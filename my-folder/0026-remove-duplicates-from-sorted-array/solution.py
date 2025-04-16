class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        S = set()
        write_index = 0
        
        for num in nums:
            if num not in S:
                nums[write_index] = num
                S.add(num)
                write_index += 1
        
        return write_index
