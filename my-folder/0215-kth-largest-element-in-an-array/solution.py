import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:]  # Copy the array
        heapq.heapify(heap)  # Convert to min-heap
        
        # Pop len(nums) - k elements to get the kth largest
        for _ in range(len(nums) - k):
            heapq.heappop(heap)
        
        return heapq.heappop(heap)  # Return the kth largest
