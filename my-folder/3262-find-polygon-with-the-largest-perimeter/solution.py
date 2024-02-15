class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        newNums = sorted(nums, reverse=True)
        goodMax = 0
        goodNums = [] 
                
        for i in (range(len(newNums))):
            if newNums[i] < sum(newNums[i+1:]):
                goodMax = newNums[i]
                break
                        
        for i in newNums:
            if i <= goodMax:
                goodNums.append(i)
                        
        if len(goodNums) == 0:
            return -1
        else: 
            return sum(goodNums)
