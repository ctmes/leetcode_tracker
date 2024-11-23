class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occurrences = {}
        for i in nums:
            if i in occurrences:
                occurrences[i] += 1
            else:
                occurrences[i] = 1

        majority = max(occurrences, key=occurrences.get)
        return majority
        
